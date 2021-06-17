from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
from .models import Item, ItemSpec
from .forms import CreateNewItem
from django.utils import timezone


# zaten eklenmiş olan öğe üzerinden listeleme ve değişiklik yapmaya yarayan fonk
def index(response, id):
    ls = Item.objects.get(id=id)
    
    if ls in response.user.item.all():
        # herhangi bir girdi var mı diye kontrol et
        if response.method == 'POST':
            print(response.POST)
            # save butonuna basıldığında;
            # ürün satıldı mı satılmadı mı o işareti kontrol et
            if response.POST.get('save'):
                if item in ls.item_set.all():
                    if response.POST.get("c" + str(item.id)) == "clicked":
                        item.sold_badge = True
                    else:
                        item.sold_badge = False
                        
                    item.save()
            
            # eğer save butonu yerine yeni öğe ekle butonuna basılırsa;
            # yeni öğe butonu veritabanına yeni bir öğe ekler
            elif response.POST.get('newItem'):
                new_item_name = response.POST.get("new")
                
                if len(new_item_name) > 2:
                    ls.item_set.create(about_item=new_item_name, sold_badge = False)
                else: print('invalid')
                
        return render(response, "root/list.html", {'ls': ls})
    return render(response, "root/home.html", {})



# ana ekran fonk
def home(response):
    return render(response, "root/home.html")

# yeni öğe oluşturmaya yarayan fonk
def create(response):
    global t
    # eğer create.html sayfası içindeki alanlar boş değilse yani validse;
    # response'un methodu 'post' olarak döner.
    # eğer method post ise;
    if response.method == 'POST':
        # form içindeki tü bilgiyi form değişkenine ata
        form = CreateNewItem(response.POST)
        
        # eğer valid değerler varsa
        if form.is_valid():
            # girilen bilgileri veritabanına kaydet
            n = form.cleaned_data["name"]
            t = Item(name=n, date=timezone.now())
            t.save()
            response.user.item.add(t)
            # kaydettikten sonra direk olarak o sayfaya git
            return HttpResponseRedirect("/%i" %t.id)
    else:
        form = CreateNewItem()
    return render(response, "root/create.html", {'form': form})

def get_name(request):
	if request.method == "POST":
		form = CreateListForm(request.POST)

		if form.is_valid():
			n = form.cleaned_data["name"]
			t = ToDoList(name=n, date=timezone.now())
			t.save()
			
			return HttpResponseRedirect("/%i" %t.id)

	else:
		form = CreateListForm()

	return render(request, "main/create.html", {"form": form})

      


def view(response):
    return render(response, "root/view.html")

def all_events(response):
    all_items = ArizaKaydi.objects.all()
    return render(response, "root/events.html", {"all_items": all_items})
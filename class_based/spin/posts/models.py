from django.db import models
# from category.models import Category
from django.utils.text import slugify
from register.models import CustomUser as User



# Create your models here.
class PostModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_user')
    title = models.CharField(max_length=120)
    about_post = models.CharField(max_length=200)
    # price = MoneyField(amount_field="fiyat", currency_field="currency")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    currency  = models.CharField(max_length=5, null=True)
    #category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='post_category')
    category = models.CharField(max_length=15)
    releaseDate = models.DateTimeField(auto_now_add=True)
    #image = models.ImageField(null=True, blank=True)
    slug = models.SlugField(unique=True, editable=False, max_length=130)

    # bu kısım update ekranınıda olması lazım
    sold_or_not_model = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_unique_slug(self):
        slug = slugify(self.title)
        unique_slug = slug
        counter = 1

        while PostModel.objects.filter(slug=unique_slug).exists():
            unique_slug = slug + "-" + str(counter)
            counter += 1

        return unique_slug

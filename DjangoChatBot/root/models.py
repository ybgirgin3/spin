from django.db import models
#from django.contrib.auth.models import User
from register.models import CustomUser as User

# kategory kısmı eklenecek onda ise şehirler olacak

# Create your models here.
class ArizaKaydi(models.Model):
    user = models.ForeignKey(User,
                            on_delete=models.CASCADE,
                            related_name="ariza",
                            null=True)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name




class Item(models.Model):
    ariza = models.ForeignKey(ArizaKaydi, on_delete=models.CASCADE)
    text = models.CharField(max_length=1000)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    complete = models.BooleanField()

    def __str__(self):
        return self.text

from django.db import models
# from django.contrib.auth.models import User
from register.models import CustomUser as User

# Create your models here.
class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="item", null=True)
    name = models.CharField(max_length=30)
    about_item = models.CharField(max_length=1000)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    sold_badge = models.BooleanField()
    
    def __str__(self):
        return self.name
    
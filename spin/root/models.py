from django.db import models
# from django.contrib.auth.models import User
from register.models import CustomUser as User

# Create your models here.
class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="item", null=True)
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name
    
    
class ItemSpec(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    about_item = models.CharField(max_length=1000)
    sold_badge = models.BooleanField()
    
    def __str__(self):
        return self.about_item
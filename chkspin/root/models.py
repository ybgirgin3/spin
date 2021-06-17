from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name
    
    
class ItemSpec(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    about_item = models.CharField(max_length=1000)
    sold_badge = models.BooleanField()
from django.db import models
from django.utils.text import slugify
# Create your models here.

# model files of Category
class Category(models.Model):
    id = models.AutoField(db_column='category_id', primary_key = True)
    title = models.CharField(max_length=120)
    image = models.FileField(null=True, blank=True)
    slug = models.SlugField(unique=True, editable=False, max_length=130)
    
    def __str__(self):
        return self.title
    

    # The slug function used to create a link.

    def get_unique_slug(self):
        slug = slugify(self.title)
        unique_slug = slug
        counter = 1

        while Category.objects.filter(slug=unique_slug).exists():
            unique_slug = slug + "-" + str(counter)
            counter += 1
        return unique_slug

    def save(self, *args, **kwargs):
        self.slug = self.get_unique_slug()

        return super(Category, self).save(*args, **kwargs)

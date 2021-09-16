from io import BytesIO
from PIL import Image
from django.core.files import File

from django.db import models
from vendor.models import Vendor



# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    ordering = models.IntegerField(default=0)

    class Meta:
        ordering = ['ordering']

    def __str__(self):
        return self.title

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendor, related_name='products', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    date_added = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='upload/', blank=True,null=True)

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return self.title

    def get_thumbnails(self):
        if self.thumbnail:
            return self.thumbnail.urls()
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()
            
                return self.thumbnail.url
            else:
                return 'http://placehold.jp/240x180.png'

    def make_thumbnail(self, image, size=(300,200)):
        img = Image.open(image)
        img.covert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, name=image.name)

        return thumbnail
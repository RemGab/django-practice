from django.db import models
from django.utils.text import slugify

# Create your models here.
class Booking(models.Model) :
    title = models.CharField(max_length=128)
    auteur= models.CharField(max_length=128, default='non référencé')
    slug = models.SlugField(max_length=255,blank=True)
    content = models.TextField(blank=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Booking, self).save(*args, **kwargs)
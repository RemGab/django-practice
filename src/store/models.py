from django.db import models
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.
class Booking(models.Model) :
    title = models.CharField(max_length=128)
    auteur= models.CharField(max_length=128, default='non référencé')
    slug = models.SlugField(max_length=255,blank=True)
    content = models.TextField(blank=True)
    
    
    class Meta :
        verbose_name = 'Article'
        ordering = ['-auteur']
    
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Booking, self).save(*args, **kwargs)
        
    def __str__(self) :
        return self.title
    
    def get_absolute_url (self):
        return reverse('store-post', kwargs={'slug': self.slug})
    
    @property
    def word_count(self):
        
        return len(self.content.split())
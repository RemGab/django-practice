from django.contrib import admin
from store.models import Booking
# Register your models here.

@admin.register(Booking)
class gestion_model(admin.ModelAdmin):
    list_display = (
        'title',
        'auteur',
        'slug',
        'truncated_content',
        'word_count'
    )
    
    empty_value_display = 'error'
    list_editable = ("auteur",'title' )
    list_display_links = ('slug', )
    search_fields = ('title','slug')
    list_per_page = 10


    
    def truncated_content(self, obj):
        return obj.content[:50] + '...' if len(obj.content) > 50 else obj.content
    truncated_content.short_description = 'Content'
    

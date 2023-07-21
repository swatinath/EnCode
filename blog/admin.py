from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from blog.models import Category, Blog

# Register your models here.

class BlogAdmin(SummernoteModelAdmin):
    list_display = ('title', 'author', 'created_at')   #used to display all the elements of the tuple
    search_fields = ('title',)
    # list_editable = ('is_available',)    #used to change is_available outside
    list_filter = ('category',)
    summernote_fields = ('description',)
    

admin.site.register(Blog, BlogAdmin)    
admin.site.register(Category)
# admin.site.register(Blog)

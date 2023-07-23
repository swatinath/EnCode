from django.forms import ModelForm
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from .models import Blog

class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = "__all__"
        widgets = {
            'description' : SummernoteWidget(),
        }
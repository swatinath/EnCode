from django import forms
from blog.models import Blog

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'author', 'description', 'image')
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Title of the Blog'}),
            'author': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Title of the Blog'}),
            # 'slug': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Copy the title with no space and a hyphen in between'}),
            'description': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Content of the Blog'}),
        }

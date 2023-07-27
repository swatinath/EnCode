from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=255)
    
    def __str__(self):
        return self.category
    class Meta:
        verbose_name_plural = "Categories"
        
class Blog(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    image = models.ImageField(upload_to="blog_images", null=True,blank=True)
    created_at = models.DateField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
        
    def __str__(self):
        return self.title   #used to display only title of the book

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    blog = models.ForeignKey(Blog, on_delete=models.DO_NOTHING, related_name='comment')
    rating = models.IntegerField()
    comment = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['created_on']
    
    def __str__(self):
        return self.blog.title+" - "+self.comment
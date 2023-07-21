from django.shortcuts import render, get_object_or_404
from blog.models import Blog, Category
# Create your views here.

def all_blogs(request):
    blogs = Blog.objects.all()
    categories = Category.objects.all().order_by('category')
    #print(books.query)
    context = {
        "blogs" : blogs,
        "categories" : categories,
    }
    return render(request, "blog/blogs.html", context)

def blog_details(request, id):
    #book = Book.objects.get(id=id)
    blog = get_object_or_404(Blog, id=id)
    context = {
        "blog" : blog
    }
    return render(request, "blog/blog.html", context)

def category_blog(request, cid):
    blogs = Blog.objects.filter(category=cid)
    categories = Category.objects.all().order_by('category')
    #print(books.query)
    context = {
        "blogs" : blogs,
        "categories" : categories,
    }
    return render(request, "blog/blogs.html", context)



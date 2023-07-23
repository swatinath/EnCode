from django.shortcuts import render, get_object_or_404, redirect
from blog.forms import BlogForm
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

def add_blogs(request):
    if request.method=="POST":
        form = BlogForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('all_blogs')
            # blogpost = form.save(commit=False)
            # blogpost.author = request.user
            # blogpost.save()
            # obj = form.instance
            # alert = True
            # return render(request, "add_blogs.html",{'obj':obj, 'alert':alert})
            # return redirect('blogs')
    else:
        form=BlogForm()
    # return redirect("all_blogs")
    return render(request, "blog/add_blogs.html", {'form':form})
    
    



from django.shortcuts import render, get_object_or_404, redirect
from blog.forms import BlogForm
from blog.models import Blog, Category, Comment
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
# Create your views here.

def all_blogs(request):
    blogs = Blog.objects.all()
    paginator = Paginator(blogs, 5)  # 18 books in each page
    page_number = request.GET.get("page")
    try:
        page_obj = paginator.get_page(page_number)
    except PageNotAnInteger:
            # If page is not an integer deliver the first page
        page_obj = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        page_obj = paginator.page(paginator.num_pages)
    categories = Category.objects.all().order_by('category')
    #print(books.query)
    context = {
        "blogs" : page_obj,
        "categories" : categories,
    }
    return render(request, "blog/blogs.html", context)

def blog_details(request, id):
    #book = Book.objects.get(id=id)
    blog = get_object_or_404(Blog, id=id)
    feedbacks = Comment.objects.filter(blog=blog)
    context = {
        "blog" : blog,
        "feedbacks" : feedbacks,
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
    
def add_feedback(request):
    if request.method == "POST":
        user = request.user
        blog_id = request.POST.get("blog_id")
        blog = Blog.objects.get(id=blog_id)
        rating = request.POST.get("rating")
        comment = request.POST.get("comment")
        feedback = None
        try:
            feedback = Comment.objects.get(user=user, blog=blog)
        except:
            print("Feedback not available")
        
        if feedback is None:
            feedback = Comment()
            feedback.user = user
            feedback.blog = blog
        feedback.rating = rating
        feedback.comment = comment
        feedback.save()
        context = {
            'blog' : blog,
            'feedback' : feedback,
        }
        return render(request, "blog/blog.html",context)    



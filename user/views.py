from django.shortcuts import render, redirect
from django.contrib.auth.models import User  #user model defined by django
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from user.forms import BlogPostForm
# Create your views here.

def signup(request):
    # if request.user:
    #     return redirect("all_blogs")
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # print(first_name, last_name, email, username, password)
        user_exists = False
        
        if User.objects.filter(username=username).exists():
            # print("Username is already taken")  #prints in console
            messages.error(request, "Username is already taken. Try with a new username.")
            user_exists = True
            
        if User.objects.filter(email=email).exists():
            # print("Email is already taken")   #prints in console
            messages.error(request, "Email is already taken")    
            user_exists = True
            
        if user_exists:    
            return render(request, 'user/signup.html')
        
        user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            email=email,
            username=username,
            password=password
        )
        user.save()
        messages.success(request, "Account created successfully. Login to continue")
    
    return render(request, 'user/signup.html')

def signin(request):
    # if request.user:
    #     return redirect("all_blogs")
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is None:
            messages.error(request, "Invalid username or password")
            return render(request, 'user/signin.html')
        
        else:
            login(request, user)
            return redirect("all_blogs")
        
    return render(request, 'user/signin.html')

    
def signout(request):
    logout(request)
    return render(request, 'user/signin.html')        


@login_required(login_url="/user/signin")
def profile(request):
    return render(request, 'user/profile.html')

def add_blog(request):
    if request.method=="POST":
        form = BlogPostForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            blogpost = form.save(commit=False)
            blogpost.author = request.user
            blogpost.save()
            obj = form.instance
            alert = True
            return render(request, "user/add_blog.html",{'obj':obj, 'alert':alert})
    else:
        form=BlogPostForm()
    return render(request, "user/add_blog.html", {'form':form})


from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment
from django.utils.timezone import now
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from materials.models import LearningMaterial
from .forms import RegistrationForm
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import CommentForm




# Create your views here.

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def coursedetails(request):
    return render(request, 'course-details.html')

def courses(request):
    return render(request, 'courses.html')

def events(request):
    return render(request, 'events.html')

def trainers(request):
    return render(request, 'trainers.html')

def starterpage(request):
    return render(request, 'starter-page.html')

def category(request):
    return render(request, 'category.html')

# Posts Page - Displays all posts
def posts(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'posts2.html', {'posts': posts, 'year': now().year})

# View a Single Post and Its Comments
def view_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = post.comments.all()
    return render(request, 'viewpost.html', {'post': post, 'comments': comments})

# Create a New Post
#@login_required
def create_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        category = request.POST.get('category')
        post = Post.objects.create(author=request.user, title=title, content=content, category=category)
        return redirect('posts')
    return render(request, 'creatpost.html')

# Add a Comment to a Post
#@login_required
def add_comment(request, post_id):
    if request.method == 'POST':
        post = get_object_or_404(Post, id=post_id)
        content = request.POST.get('comment')
        Comment.objects.create(post=post, user=request.user, content=content)
        return redirect('viewpost', post_id=post_id)

def dashboard(request):
    materials = LearningMaterial.objects.all()  # Fetch all materials
    return render(request, 'dashboard.html', {'materials': materials})

def delete_post(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect('posts2')  # Redirect to the main posts page






# Login View
"""def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'You have successfully logged in')
            return redirect('index')
        else:
            messages.error(request, 'Invalid credentials')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})"""
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Authenticate the user
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)  # Log the user in
                return redirect('index')  # Redirect to the home page
            else:
                form.add_error(None, "Invalid login credentials")
        else:
            form.add_error(None, "Form is not valid")
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})








# Logout View
def logout_view(request):
    logout(request)
    messages.success(request, 'You have successfully logged out')
    return redirect('index')  # Redirect to the home page or any page you prefer




# Registration View
def register(request):
    if request.method == 'POST':
        # Get data from the form
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')

        # Password match validation
        if password1 != password2:
            messages.error(request, 'Passwords do not match.')
            return redirect('register')

        # Create the user
        user = User.objects.create_user(username=username, password=password1)
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.save()

        # Log the user in immediately after registration
        login(request, user)
        messages.success(request, 'Registration successful!')
        return redirect('index')  # Redirect to the homepage or any other page you prefer

    return render(request, 'registration.html')  # Render the registration form


##this is the working comment 
def comment_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post  # Associate the comment with the post
            comment.author = request.user  # Associate the comment with the logged-in user
            comment.save()
            return redirect('posts')  # Redirect back to the posts page after submitting a comment
    else:
        form = CommentForm()
    return render(request, 'comment_form.html', {'form': form, 'post': post})


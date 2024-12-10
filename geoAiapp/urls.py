"""
URL configuration for geoAiProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('coursedetails/', views.coursedetails, name='coursedetails'),
    path('courses/', views.courses, name='courses'),
    path('events/', views.events, name='events'),
    path('posts/create/', views.create_post, name='create_post'),  # Page to create a post
    path('posts/<int:post_id>/', views.view_post, name='view_post'),  # View a specific post
    #path('add-comment/<int:post_id>/', views.add_comment, name='add_comment'),  # Add a comment to a post
    path('trainers/', views.trainers, name='trainers'),  # Trainers page
    path('starterpage/', views.starterpage, name='starterpage'),  # Starter page
    path('category/', views.category, name='category'),  # Category page
    path('posts/', views.posts, name='posts'),
    path('create_post/', views.create_post, name='createpost'),
    path('posts/', views.posts, name='posts2'), 
    path('post/<int:post_id>/', views.view_post, name='viewpost'),
    path('dashboard/', views.dashboard, name='dashboard'),  
    path('delete/<int:id>/', views.delete_post, name='delete_post'),
    path('register/', views.register, name='register'),
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('posts/<int:post_id>/comment/', views.comment_post, name='comment_post')
    
    
    


]

from django.contrib import admin
from django.contrib.auth.models import User  # Import the default User model
from .models import Post  # Import your models (e.g., Post, Comment)

# Register your models
admin.site.register(Post)  # Register your model for the admin panel

# You can also customize the admin panel for the default User model if needed
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('username', 'email')

admin.site.unregister(User)  # Unregister the default User model first
admin.site.register(User, UserAdmin)  # Then register it with your custom admin

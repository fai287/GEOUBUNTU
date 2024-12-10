from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import LearningMaterial

@admin.register(LearningMaterial)
class LearningMaterialAdmin(admin.ModelAdmin):
    list_display = ('title', 'uploaded_at')

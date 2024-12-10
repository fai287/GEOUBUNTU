from django import forms
from .models import LearningMaterial

class LearningMaterialForm(forms.ModelForm):
    class Meta:
        model = LearningMaterial
        fields = ['title', 'description', 'file', 'image', 'video', 'content_type']

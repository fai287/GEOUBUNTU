from django.shortcuts import render, get_object_or_404, redirect
from .models import LearningMaterial
from .forms import LearningMaterialForm
from django.contrib.auth.decorators import login_required, user_passes_test

# Check if the user is an admin
def is_admin(user):
    return user.is_staff

@login_required
@user_passes_test(is_admin)
def dashboard(request):
    if request.method == 'POST':  # Handle form submissions (upload, delete, etc.)
        if 'upload' in request.POST:  # Handle material upload
            form = LearningMaterialForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('dashboard')  # Refresh the page after upload
        elif 'delete' in request.POST:  # Handle material delete
            material_id = request.POST.get('material_id')
            material = get_object_or_404(LearningMaterial, pk=material_id)
            material.delete()
            return redirect('dashboard')  # Refresh the page after delete

    # Display the current materials
    materials = LearningMaterial.objects.all()
    return render(request, 'dashboard.html', {'materials': materials})

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.core.files.storage import FileSystemStorage
from django.conf import settings

from .models import Resume, Experience, Education, Skill, Project
from .forms import RegisterForm, ResumeForm, ExperienceForm, EducationForm # We need to create these forms

import warnings

# Try importing simple_weasyprint or weasyprint
try:
    from weasyprint import HTML, CSS
except OSError:
    warnings.warn("WeasyPrint requires GTK3 to be installed. PDF Generation might fail locally.")
    HTML = None

def register_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Error during registration')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard(request):
    resumes = request.user.resumes.all()
    return render(request, 'dashboard.html', {'resumes': resumes})

@login_required
def create_resume(request):
    resume = Resume.objects.create(user=request.user, title="My New Resume")
    return redirect('edit_resume', resume_id=resume.id)

@login_required
def edit_resume(request, resume_id):
    resume = get_object_or_404(Resume, id=resume_id, user=request.user)
    
    if request.method == 'POST':
        form = ResumeForm(request.POST, instance=resume)
        if form.is_valid():
            form.save()
            messages.success(request, 'Resume saved!')
            return redirect('edit_resume', resume_id=resume.id)
    else:
        form = ResumeForm(instance=resume)

    context = {
        'resume': resume,
        'form': form,
    }
    return render(request, 'edit_resume.html', context)

@login_required
def generate_pdf(request, resume_id):
    resume = get_object_or_404(Resume, id=resume_id, user=request.user)
    
    # Render HTML for PDF
    html_string = render_to_string('resume_pdf.html', {'resume': resume})
    
    if HTML:
        html = HTML(string=html_string, base_url=request.build_absolute_uri())
        pdf_file = html.write_pdf()
        
        response = HttpResponse(pdf_file, content_type='application/pdf')
        response['Content-Disposition'] = f'inline; filename="{resume.full_name}_Resume.pdf"'
        return response
    else:
        return HttpResponse("PDF Generation unavailable (WeasyPrint/GTK missing)", status=503)

# HTMX Views
@login_required
def htmx_add_experience(request, resume_id):
    resume = get_object_or_404(Resume, id=resume_id, user=request.user)
    if request.method == 'POST':
        form = ExperienceForm(request.POST)
        if form.is_valid():
            exp = form.save(commit=False)
            exp.resume = resume
            exp.save()
            # Return just the list of experiences to update the DOM
            return render(request, 'partials/experience_list.html', {'resume': resume})
    return HttpResponse(status=400)

@login_required
def htmx_delete_experience(request, pk):
    exp = get_object_or_404(Experience, pk=pk, resume__user=request.user)
    resume = exp.resume
    exp.delete()
    return render(request, 'partials/experience_list.html', {'resume': resume})

# Default home redirect
def home(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'home.html')

from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path("register/", views.register_view, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    
    path("dashboard/", views.dashboard, name="dashboard"),
    path("resume/create/", views.create_resume, name="create_resume"),
    path("resume/<int:resume_id>/edit/", views.edit_resume, name="edit_resume"),
    path("resume/<int:resume_id>/pdf/", views.generate_pdf, name="generate_pdf"),
    
    # HTMX
    path("resume/<int:resume_id>/experience/add/", views.htmx_add_experience, name="htmx_add_experience"),
    path("experience/<int:pk>/delete/", views.htmx_delete_experience, name="htmx_delete_experience"),
]
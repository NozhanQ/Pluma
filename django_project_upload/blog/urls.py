from django.urls import path
from . import views
from .views import register_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.post_list, name="post_list"),
    path("post/<int:pk>/", views.post_detail, name="post_detail"),
    path("post/new/", views.post_new, name="post_new"),
    path("post/<int:pk>/edit/", views.post_edit, name="post_edit"),
    path("post/<int:pk>/delete/", views.post_delete, name="post_delete"),
    path("register/", register_view, name="register"),
    path("login/", auth_views.LoginView.as_view(template_name="blog/login.html"), name='login'),
    path("logout/", auth_views.LogoutView.as_view(next_page="/"), name="logout"),
]

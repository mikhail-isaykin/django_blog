from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", LoginView.as_view(template_name='accounts/login.html'), name="login"),
    path("logout/", LoginView.as_view(next_page='home'), name="logout"),
]

from . import views
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='accounts/login.html', next_page='lista'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout')
]
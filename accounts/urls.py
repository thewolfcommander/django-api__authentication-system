from django.urls import path
from django.contrib.auth import decorators

from .views import HomeView, UserRegisterView, UserLoginView

app_name = 'home'

urlpatterns = [
    path('', decorators.login_required(HomeView.as_view(), login_url='accounts:login'), name='home'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('register/', UserRegisterView.as_view(), name='register'),
]

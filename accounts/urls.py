from django.contrib.auth import decorators
from django.urls import path

from .views import HomeView, LogoutView, UserLoginView, UserRegisterView, CompleteProfileView

app_name = 'home'

urlpatterns = [
    path('', decorators.login_required(HomeView.as_view(), login_url='accounts:login'), name='home'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('complete/', CompleteProfileView.as_view(), name='complete_profile'),
    path('register/', UserRegisterView.as_view(), name='register'),
]

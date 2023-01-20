from django.urls import path
from .views import HomeView, UserRegisterView, UserLoginView

app_name = 'home'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('register/', UserRegisterView.as_view(), name='register'),
]

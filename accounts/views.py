from django.contrib.auth import decorators, login, logout, models
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import FormView, TemplateView, UpdateView

from .forms import UserLoginForm, UserRegisterForm


# Create your views here.
class HomeView(TemplateView):
    template_name = "accounts/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # add any additional context data here
        if self.request.user.is_authenticated:
            context['user'] = self.request.user
        return context


class UserLoginView(FormView):
    form_class = UserLoginForm
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('accounts:home')

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super().form_valid(form)


class UserRegisterView(FormView):
    form_class = UserRegisterForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('accounts:home')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)
    

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('accounts:login')  # or any other page
    



@method_decorator(login_required, name='dispatch')
class CompleteProfileView(UpdateView):
    model = models.User
    fields = ['first_name', 'last_name']  # add fields you want to include in the form
    template_name = 'accounts/complete_profile.html'
    success_url = reverse_lazy('accounts:home')  # change to where you want to redirect after successful form submission

    def get_object(self, queryset=None):
        return self.request.user  # assumes 'profile' attribute on your user model


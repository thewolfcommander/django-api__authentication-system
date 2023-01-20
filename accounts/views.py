from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView

from .forms import UserLoginForm, UserRegisterForm


# Create your views here.
class HomeView(TemplateView):
    template_name = "accounts/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # add any additional context data here
        return context



class UserLoginView(FormView):
    form_class = UserLoginForm
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super().form_valid(form)

class UserRegisterView(FormView):
    form_class = UserRegisterForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)

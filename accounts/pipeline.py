from django.shortcuts import redirect
from django.urls import reverse

def redirect_to_profile_completion(backend, user, response, *args, **kwargs):
    # Only redirect for new users
    if kwargs['is_new']:
        return redirect(reverse('accounts:complete_profile'))

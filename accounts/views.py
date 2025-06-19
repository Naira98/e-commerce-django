from django.shortcuts import render
from django.views.generic import CreateView

from .models import CustomUser
from .froms import UserForm


class RegisterView(CreateView):
    model = CustomUser
    form_class = UserForm
    template_name = "registration/register.html"
    success_url = "/login"

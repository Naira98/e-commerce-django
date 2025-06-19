from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import CustomUser
from .froms import UserForm, UserEditForm


class RegisterView(CreateView):
    model = CustomUser
    form_class = UserForm
    template_name = "registration/register.html"
    success_url = "/login"


class UpdateProfile(UpdateView):
    model = CustomUser
    template_name = "registration/edit_profile.html"
    form_class = UserEditForm
    success_url = "/profile"

    def get_object(self, queryset=None):
        return self.request.user



class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "registration/profile.html"

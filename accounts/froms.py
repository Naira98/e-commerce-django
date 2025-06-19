from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, SetPasswordMixin
from django.contrib.auth.hashers import make_password
from .models import CustomUser


class UserForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("username", "email", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Tailwind-style classes for all fields
        for field_name, field in self.fields.items():
            field.widget.attrs.update(
                {
                    "class": "w-full px-4 py-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-yellow-400 focus:border-yellow-400",
                }
            )


class UserEditForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ["first_name", "last_name", "profile_picture"]

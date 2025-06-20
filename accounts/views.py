from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status


from .models import CustomUser
from .froms import UserForm, UserEditForm
from .models import Product


class RegisterView(CreateView):
    model = CustomUser
    form_class = UserForm
    template_name = "registration/register.html"
    success_url = "/accounts/login"


class UpdateProfile(UpdateView):
    model = CustomUser
    template_name = "registration/edit_profile.html"
    form_class = UserEditForm
    success_url = "/accounts/profile"

    def get_object(self, queryset=None):
        return self.request.user


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "registration/profile.html"


class FavoritesView(LoginRequiredMixin, TemplateView):
    template_name = "registration/favorites.html"



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def toggle_favorite(request):
    product_id = request.data.get('product_id')

    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return Response({'error': 'Product not found'}, status=404)

    user = request.user

    if product in user.favorites.all():
        user.favorites.remove(product)
        return Response({'status': 'removed', 'is_favorite': False})
    else:
        user.favorites.add(product)
        return Response({'status': 'added', 'is_favorite': True})


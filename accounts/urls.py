from django.urls import path, include
from . import views

urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path("register/", views.RegisterView.as_view(), name="register"),
    path("profile/", views.ProfileView.as_view(), name="profile"),
    path("profile/edit", views.UpdateProfile.as_view(), name="edit_profile"),
    
    path("favorites", views.FavoritesView.as_view(), name="favorites"),
    path("toggle-favorite", views.toggle_favorite, name="toggle-favorite"),
]

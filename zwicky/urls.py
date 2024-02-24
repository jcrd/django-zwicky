from django.urls import include, path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("signup/", views.signup, name="signup"),
    path("account/", include("django.contrib.auth.urls")),
]

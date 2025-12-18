from django.urls import path
from .views import profile_me

urlpatterns = [
    path("me/", profile_me),
]

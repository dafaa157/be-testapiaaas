from django.urls import path
from .views import profile_me, list_students, profile_detail

urlpatterns = [
    path("me/", profile_me),
    path("list/", list_students),
    path("<str:nim>/", profile_detail),
]

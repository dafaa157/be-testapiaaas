from django.urls import path
from .views import  list_students, profile_detail

urlpatterns = [
    path("list/", list_students),
    path("<str:nim>/", profile_detail),
]

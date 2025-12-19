from django.urls import path
from .views import profile_me, list_students

urlpatterns = [
    path("me/", profile_me),
    path("list/", list_students),
    path("<str:nim>/", profile_detail),
]

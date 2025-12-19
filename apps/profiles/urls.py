from django.urls import path
from .views import profile_me, list_students, student_detail

urlpatterns = [
    path("me/", profile_me, name="profile_me"),
    path("list/", list_students, name="list_students"),
    path("detail/<str:nim>/", student_detail, name="student_detail"),
]

from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import login_view, register_view, me_view

urlpatterns = [
    path("login/", login_view),
    path("register/", register_view),
    path("me/", me_view),
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]

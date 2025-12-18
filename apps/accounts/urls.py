from django.urls import path
from .views import login_view, register_view, me_view

urlpatterns = [
    path('login/', login_view),
    path('register/', register_view),
    path('me/', me_view),
]
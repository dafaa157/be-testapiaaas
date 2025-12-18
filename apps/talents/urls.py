from django.urls import path
from .views import skill_list_create, experience_list_create, portfolio_list_create


urlpatterns = [
    path("skills/", skill_list_create),
    path("experiences/", experience_list_create),
    path("portfolios/", portfolio_list_create),
]

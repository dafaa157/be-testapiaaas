from django.urls import path

from .views import (
    skill_list_create,
    experience_list_create,
    portfolio_list_create,
    public_skills,
    public_experiences,
    public_portfolios,
    experience_detail,
    skill_detail,

)

urlpatterns = [
    path("skills/", skill_list_create),
    path("skills/<int:pk>/", skill_detail),
    path("experiences/", experience_list_create),
    path("experiences/<int:pk>/", experience_detail),
    path("portfolios/", portfolio_list_create),

    path("<str:nim>/skills/", public_skills),
    path("<str:nim>/experiences/", public_experiences),
    path("<str:nim>/portfolios/", public_portfolios),
]

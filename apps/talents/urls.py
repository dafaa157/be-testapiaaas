from .views import (
    skill_list_create,
    experience_list_create,
    portfolio_list_create,
    public_skills,
    public_experiences,
    public_portfolios
)

urlpatterns = [
    path("skills/", skill_list_create),
    path("experiences/", experience_list_create),
    path("portfolios/", portfolio_list_create),

    path("<str:nim>/skills/", public_skills),
    path("<str:nim>/experiences/", public_experiences),
    path("<str:nim>/portfolios/", public_portfolios),
]

from django.db import models
from apps.profiles.models import StudentProfile

class Skill(models.Model):
    name = models.CharField(max_length=100)
    student = models.ManyToManyField(StudentProfile, related_name="skills")

    def __str__(self):
        return self.name


class Experience(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE, related_name="experiences")
    title = models.CharField(max_length=120)
    institution = models.CharField(max_length=120)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    is_current = models.BooleanField(default=False)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title


class Portfolio(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE, related_name="portfolios")
    title = models.CharField(max_length=120)
    link = models.URLField(blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title

from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nim = models.CharField(max_length=20, unique=True)
    full_name = models.CharField(max_length=150)
    prodi = models.CharField(max_length=120, blank=True)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to="profiles/", blank=True, null=True)
    
    phone = models.CharField(max_length=20, default='')


    custom_cv_file = CloudinaryField(
        "CV File", 
        resource_type="raw", 
        folder="cv_uploads",
        blank=True, 
        null=True
    )
    
    email = models.EmailField(max_length=100, blank=True, null=True)     # Email Publik
    linkedin = models.URLField(max_length=200, blank=True, null=True)    # Link LinkedIn
    github = models.URLField(max_length=200, blank=True, null=True)      # Link GitHub
    instagram = models.URLField(max_length=200, blank=True, null=True)   # Link Instagram
    def __str__(self):
        return self.full_name

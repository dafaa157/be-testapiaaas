from rest_framework import serializers
from .models import StudentProfile


class StudentProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentProfile
        fields = ["id", "full_name", "nim", "prodi", "bio", "profile_picture"]

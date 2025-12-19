from rest_framework import serializers
from .models import StudentProfile
from apps.talents.serializers import SkillSerializer, ExperienceSerializer, PortfolioSerializer

class StudentProfileSerializer(serializers.ModelSerializer):
    skills = SkillSerializer(many=True, read_only=True)
    experiences = ExperienceSerializer(many=True, read_only=True)
    portfolios = PortfolioSerializer(many=True, read_only=True)
    
    class Meta:
        model = StudentProfile
        fields = fields = [
            "id",
            "full_name",
            "nim",
            "prodi",
            "bio",
            "profile_picture",

        ]

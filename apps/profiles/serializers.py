from rest_framework import serializers
from .models import StudentProfile

from apps.talents.serializers import SkillSerializer, ExperienceSerializer, PortfolioSerializer

class StudentProfileSerializer(serializers.ModelSerializer):
    # Make profile_picture URL readable
    profile_picture = serializers.ImageField(required=False)
    skills = SkillSerializer(many=True, read_only=True)
    experiences = ExperienceSerializer(many=True, read_only=True)
    portfolios = PortfolioSerializer(many=True, read_only=True)
    
    class Meta:
        model = StudentProfile
        fields = ["id", "full_name", "nim", "prodi", "bio", "profile_picture", "phone","skills", "experiences", "portfolios"]
        # Make these optional when updating
        extra_kwargs = {
            'phone': {'required': False},
            'bio': {'required': False},
            'prodi': {'required': False},
        }

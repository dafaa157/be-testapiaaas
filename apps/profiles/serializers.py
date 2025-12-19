from rest_framework import serializers
from .models import StudentProfile


class StudentProfileSerializer(serializers.ModelSerializer):
    # Make profile_picture URL readable
    profile_picture = serializers.ImageField(required=False)
    
    class Meta:
        model = StudentProfile
        fields = ["id", "full_name", "nim", "prodi", "bio", "profile_picture", "phone"]
        # Make these optional when updating
        extra_kwargs = {
            'phone': {'required': False},
            'bio': {'required': False},
            'prodi': {'required': False},
        }

from rest_framework import serializers
from django.contrib.auth.models import User


class RegisterSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(write_only=True)
    nim = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["id", "full_name", "nim", "email", "password"]

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["nim"],     # gunakan nim sbg username
            email=validated_data["email"],
            password=validated_data["password"],
        )

        # optional: simpan nama (boleh hapus kalau tidak perlu)
        user.first_name = validated_data["full_name"]
        user.save()

        return user

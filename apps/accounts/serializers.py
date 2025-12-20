from rest_framework import serializers
from django.contrib.auth.models import User

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        
        # 👇 TAMBAHKAN INI: Masukkan info status user ke response
        data['is_superuser'] = self.user.is_superuser
        data['email'] = self.user.email
        data['full_name'] = self.user.studentprofile.full_name if hasattr(self.user, 'studentprofile') else "Admin"
        
        return data
        
class RegisterSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["id", "email", "password", "full_name"]

    def create(self, validated_data):
        full_name = validated_data.pop("full_name")
        email = validated_data.get("email")
        password = validated_data.get("password")

        # username = pakai email biar gak wajib input lain
        username = email  

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=full_name,   # simpan full name *tanpa dipecah*
        )
        return user


class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ["id", "email", "full_name"]

    def get_full_name(self, obj):
        return obj.first_name

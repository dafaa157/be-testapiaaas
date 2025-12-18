from django.shortcuts import render

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated

@api_view(['POST'])
def login_view(request):
    identifier = request.data.get('identifier')   
    password = request.data.get('password')

    if not identifier or not password:
        return Response(
            {"detail": "Email/Username dan password wajib diisi"},
            status=status.HTTP_400_BAD_REQUEST
        )

    
    if '@' in identifier:
        try:
            user_obj = User.objects.get(email=identifier)
            username = user_obj.username
        except User.DoesNotExist:
            return Response({"detail": "Email tidak ditemukan"}, status=status.HTTP_401_UNAUTHORIZED)
    else:
        username = identifier

    # autentikasi django
    user = authenticate(username=username, password=password)

    if user is None:
        return Response(
            {"detail": "Email/Username atau password salah"},
            status=status.HTTP_401_UNAUTHORIZED
        )

    refresh = RefreshToken.for_user(user)

    return Response({
        "access": str(refresh.access_token),
        "refresh": str(refresh),
        "user": {
            "id": user.id,
            "email": user.email,
            "username": user.username,
            "is_staff": user.is_staff
        }
    })

@api_view(['POST'])
def register_view(request):
    email = request.data.get('email')
    password = request.data.get('password')
    full_name = request.data.get('full_name')
    nim = request.data.get('nim')

    if not all([email, password, full_name, nim]):
        return Response(
            {"detail": "Semua field wajib diisi"},
            status=status.HTTP_400_BAD_REQUEST
        )

    if User.objects.filter(username=email).exists():
        return Response(
            {"detail": "Email sudah terdaftar"},
            status=status.HTTP_400_BAD_REQUEST
        )

    # create auth user
    user = User.objects.create_user(
        username=email,
        email=email,
        password=password
    )

    # create profile
    from apps.profiles.models import StudentProfile
    StudentProfile.objects.create(
        user=user,
        full_name=full_name,
        nim=nim,
        prodi="",  
        bio=""
    )

    return Response(
        {"detail": "Register berhasil"},
        status=status.HTTP_201_CREATED
    )



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def me_view(request):
    user = request.user
    return Response({
        "id": user.id,
        "email": user.email,
        "is_staff": user.is_staff
    })

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from .serializers import RegisterSerializer, UserSerializer
from apps.profiles.models import StudentProfile

from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import MyTokenObtainPairSerializer 

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

@api_view(["POST"])
def register_view(request):
    serializer = RegisterSerializer(data=request.data)

    if serializer.is_valid():
        user = serializer.save()
        
        # AUTO-CREATE StudentProfile
        StudentProfile.objects.create(
            user=user,
            nim=request.data.get('nim', ''),
            full_name=request.data.get('full_name', user.username),
            prodi=request.data.get('prodi', ''),
            phone=request.data.get('phone', ''),
            bio=''
        )
        
        return Response(
            {
                "detail": "Register berhasil",
                "user": UserSerializer(user).data,
            },
            status=status.HTTP_201_CREATED,
        )

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def login_view(request):
    identifier = request.data.get("identifier")
    password = request.data.get("password")

    if not identifier or not password:
        return Response(
            {"detail": "Email/Username dan password wajib diisi"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    # login pakai email atau username
    if "@" in identifier:
        try:
            user_obj = User.objects.get(email=identifier)
            username = user_obj.username
        except User.DoesNotExist:
            return Response({"detail": "Email tidak ditemukan"}, status=status.HTTP_401_UNAUTHORIZED)
    else:
        username = identifier

    user = authenticate(username=username, password=password)

    if user is None:
        return Response(
            {"detail": "Email/Username atau password salah"},
            status=status.HTTP_401_UNAUTHORIZED,
        )

    refresh = RefreshToken.for_user(user)

    return Response(
        {
            "access": str(refresh.access_token),
            "refresh": str(refresh),
            "user": UserSerializer(user).data,
        }
    )


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def me_view(request):
    serializer = UserSerializer(request.user)
    return Response(serializer.data)

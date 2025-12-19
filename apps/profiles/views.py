from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status

from .models import StudentProfile
from .serializers import StudentProfileSerializer


@api_view(["GET", "PUT"])
@permission_classes([IsAuthenticated])
def profile_me(request):
    profile = StudentProfile.objects.get(user=request.user)

    if request.method == "GET":
        serializer = StudentProfileSerializer(profile)
        return Response(serializer.data)

    if request.method == "PUT":
        serializer = StudentProfileSerializer(profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
@permission_classes([AllowAny]) # Bisa diganti AllowAny kalau mau public
def list_students(request):
    # Ambil semua data student
    profiles = StudentProfile.objects.all()
    
    # Serialize datanya (many=True itu wajib karena datanya list/banyak)
    serializer = StudentProfileSerializer(profiles, many=True)
    
    return Response(serializer.data)

@api_view(["GET"])
@permission_classes([AllowAny])
def profile_detail(request, nim):
    try:
        profile = StudentProfile.objects.get(nim=nim)
    except StudentProfile.DoesNotExist:
        return Response({"detail": "Student not found"}, status=404)

    serializer = StudentProfileSerializer(profile)
    return Response(serializer.data)

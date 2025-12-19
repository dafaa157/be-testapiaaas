from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status

from .models import StudentProfile
from .serializers import StudentProfileSerializer


@api_view(["GET", "PUT"])
@permission_classes([IsAuthenticated])
def profile_me(request):
    try:
        profile = StudentProfile.objects.get(user=request.user)
    except StudentProfile.DoesNotExist:
        return Response(
            {"detail": "Profile tidak ditemukan"}, 
            status=status.HTTP_404_NOT_FOUND
        )

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
@permission_classes([AllowAny])
def list_students(request):
    """Endpoint untuk list semua student dengan skills, experiences, portfolios"""
    profiles = StudentProfile.objects.all()
    serializer = StudentProfileSerializer(profiles, many=True)
    return Response(serializer.data)


@api_view(["GET"])
@permission_classes([AllowAny])
def student_detail(request, nim):
    """Endpoint untuk detail student berdasarkan NIM"""
    try:
        profile = StudentProfile.objects.get(nim=nim)
        serializer = StudentProfileSerializer(profile)
        return Response(serializer.data)
    except StudentProfile.DoesNotExist:
        return Response(
            {"detail": "Student dengan NIM tersebut tidak ditemukan"}, 
            status=status.HTTP_404_NOT_FOUND
        )

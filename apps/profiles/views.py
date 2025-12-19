
from rest_framework.decorators import (
    api_view,
    permission_classes,
    authentication_classes,
)
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .models import StudentProfile
from .serializers import StudentProfileSerializer

@api_view(["GET", "PUT"])
@permission_classes([IsAuthenticated])
def profile_me(request):
    profile, created = StudentProfile.objects.get_or_create(user=request.user)

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
@authentication_classes([])      # matikan JWT auth
@permission_classes([AllowAny])  # public endpoint
def list_students(request):
    profiles = StudentProfile.objects.all()
    serializer = StudentProfileSerializer(profiles, many=True)
    return Response(serializer.data)


@api_view(["GET"])
@authentication_classes([])      # matikan JWT auth
@permission_classes([AllowAny])  # public endpoint
def profile_detail(request, nim):
    try:
        profile = StudentProfile.objects.get(nim=nim)
    except StudentProfile.DoesNotExist:
        return Response({"detail": "Student not found"}, status=404)

    serializer = StudentProfileSerializer(profile)
    return Response(serializer.data)

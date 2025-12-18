from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from apps.profiles.models import StudentProfile
from .models import Skill, Experience, Portfolio
from .serializers import SkillSerializer, ExperienceSerializer, PortfolioSerializer


@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def skill_list_create(request):
    profile = StudentProfile.objects.get(user=request.user)

    if request.method == "GET":
        skills = profile.skills.all()
        serializer = SkillSerializer(skills, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = SkillSerializer(data=request.data)
        if serializer.is_valid():
            skill = serializer.save()
            profile.skills.add(skill)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def experience_list_create(request):
    profile = StudentProfile.objects.get(user=request.user)

    if request.method == "GET":
        experiences = profile.experiences.all()
        serializer = ExperienceSerializer(experiences, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = ExperienceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(student=profile)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def portfolio_list_create(request):
    profile = StudentProfile.objects.get(user=request.user)

    if request.method == "GET":
        portfolios = profile.portfolios.all()
        serializer = PortfolioSerializer(portfolios, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = PortfolioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(student=profile)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

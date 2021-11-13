from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import CourseSerializers
from rest_framework.viewsets import ModelViewSet
from .models import CourseModel
from rest_framework.permissions import IsAdminUser, IsAuthenticated

# Views here
class CourseListView(ModelViewSet):
    permission_classes = [IsAuthenticated, IsAdminUser]
    serializer_class = CourseSerializers
    queryset = CourseModel.objects.all()

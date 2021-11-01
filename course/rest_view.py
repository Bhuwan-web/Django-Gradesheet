from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import CourseSerializers
from rest_framework.viewsets import ModelViewSet
from .models import CourseModel

# Views here
class CourseListView(ModelViewSet):
    serializer_class = CourseSerializers
    queryset = CourseModel.objects.all()

from django.db.models import fields
from rest_framework import serializers
from rest_framework.viewsets import ModelViewSet
from .models import TeachersInfoModel, UserAdmission, UserInfo, ParentsInfo, StudentInfo


class UserInfoSerlizer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = "__all__"


class StudentInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentInfo
        fields = "__all__"


class ParentsInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParentsInfo
        fields = "__all__"


class TeachersInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeachersInfoModel
        fields = "__all__"


class AdmissionSerializer(serializers.ModelSerializer):
    basic_info = UserInfoSerlizer()
    student_info = StudentInfoSerializer()
    parents_info = ParentsInfoSerializer()

    class Meta:
        model = UserAdmission
        fields = "__all__"

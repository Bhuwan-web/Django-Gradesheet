from django.contrib import admin
from .models import UserInfo,StudentInfo,ParentsInfo,UserAdmission
# Register your models here.
admin.site.register([UserInfo,StudentInfo,ParentsInfo,UserAdmission])
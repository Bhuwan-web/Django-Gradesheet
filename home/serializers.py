from django.http import response
from django.shortcuts import render
from rest_framework.response import Response
from admission.models import UserAdmission
from admission.teachers_model import TeachersInfoModel
from course.models import CourseModel
from rest_framework.decorators import api_view
from rest_framework import serializers

# Create your views here
class HomeSerializer(serializers.Serializer):
    def trial(teacherInfo):
        heading = {"Grade": "Subjects"}
        subs1 = list()
        subs2 = list()
        subs3 = list()
        subs4 = list()
        subs5 = list()
        subs6 = list()
        subs7 = list()
        subs8 = list()
        subs9 = list()
        subs10 = list()
        subs11 = list()
        subs12 = list()
        subs = [heading]
        i = 0
        j = 10
        k = 20
        try:
            try:
                subs1 = [{sub.grade: sub.sub1} for sub in teacherInfo.sub1.all()]
                subs.extend(subs1)

            except:
                pass
            try:
                subs2 = [{sub.grade: sub.sub2} for sub in teacherInfo.sub2.all()]
                subs.extend(subs2)
            except:
                pass
            try:
                subs3 = [{sub.grade: sub.sub3} for sub in teacherInfo.sub3.all()]
                subs.extend(subs3)
            except:
                pass
            try:
                subs4 = [{sub.grade: sub.sub4} for sub in teacherInfo.sub4.all()]
                subs.extend(subs4)

            except:
                pass
            try:
                subs5 = [{sub.grade: sub.sub5} for sub in teacherInfo.sub5.all()]
                subs.extend(subs5)
            except:
                pass
            try:
                subs6 = [{sub.grade: sub.sub6} for sub in teacherInfo.sub6.all()]
                subs.extend(subs6)

            except:
                pass
            try:
                subs7 = [{sub.grade: sub.sub7} for sub in teacherInfo.sub7.all()]
                subs.extend(subs7)

            except:
                pass
            try:
                subs8 = [{sub.grade: sub.sub8} for sub in teacherInfo.sub8.all()]
                subs.extend(subs8)

            except:
                pass
            try:
                subs9 = [{sub.grade: sub.sub9} for sub in teacherInfo.sub9.all()]
                subs.extend(subs9)

            except:
                pass
            try:
                subs10 = [{sub.grade: sub.sub10} for sub in teacherInfo.sub10.all()]
                subs.extend(subs10)

            except:
                pass
            try:
                subs11 = [{sub.grade: sub.sub11} for sub in teacherInfo.sub11.all()]
                subs.extend(subs11)

            except:
                pass

            try:
                subs12 = [{sub.grade: sub.sub12} for sub in teacherInfo.sub12.all()]
                subs.extend(subs12)

            except:
                pass
        except:
            pass
        finally:
            return subs

    # For student.......
    try:
        admissionInfo = UserAdmission.objects.get(student_info__email=request.user.email)
        subject_info = dict()
        teacher_info = dict()

        try:
            course_info = CourseModel.objects.get(grade=admissionInfo.student_info.grade)
            for k, v in course_info.__dict__.items():
                if "tec" in k and v != None:
                    print(k, v)
                    teacher = TeachersInfoModel.objects.get(id=v)
                    teacher_info[k] = teacher
            for k, v in course_info.__dict__.items():
                if "sub" in k and v != None:
                    subject_info[k] = v

        except:
            pass
        context = {
            "admissionInfo": admissionInfo,
            "userInfo": admissionInfo.basic_info,
            "student_info": admissionInfo.student_info,
            "parents_info": admissionInfo.parents_info,
            "subjects_info_dict": subject_info,
            "teachers_info_dict": teacher_info,
        }
    except:
        # For Teachers
        try:
            teacherInfo = TeachersInfoModel.objects.get(email=request.user.email)
            subs = list()
            try:
                subs = trial(teacherInfo)
            except:
                pass
            finally:
                userInfo = teacherInfo
                subjects = subs
        except:
            admissionInfos = UserAdmission.objects.filter(parents_info__email=request.user.email)
            userInfo = (admissionInfos[0].parents_info,)
            studentAdmissionDetails = ([admissionInfo for admissionInfo in admissionInfos],)
            students_info = ([admissionInfo.student_info for admissionInfo in admissionInfos],)

    finally:
        # return render(request, "home/home.html", context)

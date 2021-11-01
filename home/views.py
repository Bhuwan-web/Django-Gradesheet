from django.http import response
from django.shortcuts import render
from admission.models import TeachersInfoModel, UserAdmission


# Create your views here.
def home(request):
    try:
        admissionInfo = UserAdmission.objects.get(student_info__email=request.user.email)
        context = {
            "admissionInfo": admissionInfo,
            "userInfo": admissionInfo.basic_info,
            "student_info": admissionInfo.student_info,
            "parents_info": admissionInfo.parents_info,
        }
    except:
        try:
            teacherInfo = TeachersInfoModel.objects.get(email=request.user.email)
            context = {"userInfo": teacherInfo}
        except:
            admissionInfos = UserAdmission.objects.filter(parents_info__email=request.user.email)
            context = {
                "userInfo": admissionInfos[0].parents_info,
                "studentAdmissionDetails": [admissionInfo for admissionInfo in admissionInfos],
                "students_info": [admissionInfo.student_info for admissionInfo in admissionInfos],
            }

    finally:
        return render(request, "home/home.html", context)

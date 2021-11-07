from django.http.response import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from admission.models import User, UserAdmission
from course.models import CourseModel
from admission.teachers_model import TeachersInfoModel


class HomeAPIView(APIView):
    def query_dict(self, custom_queryset, field_list):
        data = dict()
        data = {field_list[i]: custom_queryset.__dict__[field_list[i]] for i in range(len(field_list))}
        return data

    @property
    def is_student(self):
        try:
            admissionInfo = UserAdmission.objects.get(student_info__email=self.request.user.email)
            return {"query": admissionInfo, "value": True}
        except:
            return {"query": "", "value": False}

    @property
    def is_teacher(self):
        try:
            teacherInfo = TeachersInfoModel.objects.get(email=self.request.user.email)
            return {"query": teacherInfo, "value": True}
        except:
            return {"query": "", "value": False}

    @property
    def is_parents(self):
        try:
            admissionInfo = UserAdmission.objects.get(parents_info__email=self.request.user.email)
            return {"query": admissionInfo, "value": True}
        except:
            return {"query": "", "value": False}

    def studentAPI(self, admissionInfo):
        subject_info = dict()
        teacher_info = dict()
        try:
            course_info = CourseModel.objects.get(grade=admissionInfo.student_info.grade)
            for k, v in course_info.__dict__.items():
                if "tec" in k and v != None:
                    teacher = TeachersInfoModel.objects.get(id=v)
                    teacher_info[k] = self.query_dict(teacher, ["f_name", "l_name", "email", "contact_no"])
            for k, v in course_info.__dict__.items():
                if "sub" in k and v != None:
                    subject_info[k] = v

        except:
            print("course format didn't get validated")
            pass
        fields = ["f_name", "l_name", "email", "contact_no"]
        parents_info = self.query_dict(admissionInfo.parents_info, fields)
        return Response(
            {"subjects_info_dict": subject_info, "teachers_info": teacher_info, "parents_info": parents_info}
        )

    def teacher_subjects(self, subs, query, manager):

        subj = [{"grade": sub.grade, "subject": sub.obj(manager)} for sub in query.obj(manager).all()]
        subs.extend(subj)

    def teacherAPI(self, teacher_info):
        subs = list()
        # print(teacher_info.related_name)
        teacher_info_fileds = ["f_name", "l_name", "email", "contact_no"]
        teacher_info_dict = self.query_dict(teacher_info, teacher_info_fileds)
        subs.extend([{"grade": sub.grade, "subject": sub.sub1} for sub in teacher_info.sub1.all()])
        subs.extend([{"grade": sub.grade, "subject": sub.sub2} for sub in teacher_info.sub2.all()])
        subs.extend([{"grade": sub.grade, "subject": sub.sub3} for sub in teacher_info.sub3.all()])
        subs.extend([{"grade": sub.grade, "subject": sub.sub4} for sub in teacher_info.sub4.all()])
        subs.extend([{"grade": sub.grade, "subject": sub.sub5} for sub in teacher_info.sub5.all()])
        subs.extend([{"grade": sub.grade, "subject": sub.sub6} for sub in teacher_info.sub6.all()])
        subs.extend([{"grade": sub.grade, "subject": sub.sub7} for sub in teacher_info.sub7.all()])
        subs.extend([{"grade": sub.grade, "subject": sub.sub8} for sub in teacher_info.sub8.all()])
        subs.extend([{"grade": sub.grade, "subject": sub.sub9} for sub in teacher_info.sub9.all()])
        subs.extend([{"grade": sub.grade, "subject": sub.sub10} for sub in teacher_info.sub10.all()])
        subs.extend([{"grade": sub.grade, "subject": sub.sub11} for sub in teacher_info.sub11.all()])
        subs.extend([{"grade": sub.grade, "subject": sub.sub12} for sub in teacher_info.sub12.all()])

        return Response({"user_info": teacher_info_dict, "subjects": subs})

    def parentsAPI(self, query):
        all_students = UserAdmission.objects.filter(parents_info=query.parents_info)
        user_info = self.query_dict(query.parents_info, ["f_name", "l_name", "contact_no", "email"])
        children = list()
        children.extend(
            [
                self.query_dict(child.basic_info, ["f_name", "l_name", "address", "date_of_birth"])
                for child in all_students
            ]
        )
        children_std_infos = list()
        children_std_infos.extend(
            [
                self.query_dict(child.student_info, ["grade", "section", "roll_no", "student_id", "email"])
                for child in all_students
            ]
        )

        return Response({"user_info": user_info, "children": children, "children_std_infos": children_std_infos})

    def get(self, request, format=None):
        # For student.......
        if self.is_student["value"] == True:
            return self.studentAPI(self.is_student["query"])
        elif self.is_teacher["value"] == True:
            return self.teacherAPI(self.is_teacher["query"])
        elif self.is_parents["value"] == True:
            return self.parentsAPI(self.is_parents["query"])
        else:
            return Response({"Error": "The logged in user is neither student nor teacher"})

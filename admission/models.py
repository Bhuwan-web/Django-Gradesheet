# from _typeshed import Self
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from course.models import CourseModel

User = get_user_model()
# Create your models here.
class UserInfo(models.Model):
    f_name = models.CharField(_("First Name: "), max_length=50)
    l_name = models.CharField(_("Last Name: "), max_length=50)
    address = models.CharField(_("Address: "), max_length=100)
    date_of_birth = models.DateField(_("DOB: "))

    def __str__(self):
        return self.f_name


class StudentInfo(models.Model):

    grade = models.CharField(_("Grade: "), max_length=50)
    section = models.CharField(_("Section: "), max_length=50)
    roll_no = models.IntegerField(blank=True, null=True)
    student_id = models.IntegerField(unique=True)
    course = models.ForeignKey(CourseModel, null=True, on_delete=models.DO_NOTHING)
    email = models.EmailField(_("Email Id:"), max_length=254, unique=True)

    def __str__(self):
        return self.grade + self.section + " " + self.email

    def clean_student_id(self):
        self.student_id = self.pk
        return self.student_id

    def clean_course(self):
        if self.course == "NULL":
            self.course_id = self.grade
            return self.course


class ParentsInfo(models.Model):
    f_name = models.CharField(_("First Name: "), max_length=50)
    l_name = models.CharField(_("Last Name: "), max_length=50)
    contact_no = models.CharField(_("Contact number"), max_length=50)
    role = "parents"
    email = models.EmailField(_("Email Id: "), max_length=254, unique=True)

    def __str__(self):
        return self.f_name


class UserAdmission(models.Model):
    basic_info = models.OneToOneField(UserInfo, on_delete=models.CASCADE)
    student_info = models.OneToOneField(
        StudentInfo,
        on_delete=models.CASCADE,
    )
    parents_info = models.ForeignKey(ParentsInfo, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.basic_info.f_name + "" + self.student_info.grade + self.student_info.section

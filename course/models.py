from django.db import models
from django.utils.translation import gettext_lazy as _

from admission.teachers_model import TeachersInfoModel

# Create your models here.
class CourseModel(models.Model):
    name = models.CharField(_("Course Name"), max_length=50)
    grade = models.IntegerField(_("Grade"))
    sub1 = models.CharField(_("Subject 1"), max_length=50, blank=True, null=True)
    tec1 = models.ForeignKey(TeachersInfoModel, on_delete=models.DO_NOTHING, null=True, blank=True, related_name="sub1")
    sub2 = models.CharField(_("Subject 2"), max_length=50, blank=True, null=True)
    tec2 = models.ForeignKey(TeachersInfoModel, on_delete=models.DO_NOTHING, null=True, blank=True, related_name="sub2")
    sub3 = models.CharField(_("Subject 3"), max_length=50, blank=True, null=True)
    tec3 = models.ForeignKey(TeachersInfoModel, on_delete=models.DO_NOTHING, null=True, blank=True, related_name="sub3")
    sub4 = models.CharField(_("Subject 4"), max_length=50, blank=True, null=True)
    tec4 = models.ForeignKey(TeachersInfoModel, on_delete=models.DO_NOTHING, null=True, blank=True, related_name="sub4")
    sub5 = models.CharField(_("Subject 5"), max_length=50, blank=True, null=True)
    tec5 = models.ForeignKey(TeachersInfoModel, on_delete=models.DO_NOTHING, null=True, blank=True, related_name="sub5")
    sub6 = models.CharField(_("Subject 6"), max_length=50, blank=True, null=True)
    tec6 = models.ForeignKey(TeachersInfoModel, on_delete=models.DO_NOTHING, null=True, blank=True, related_name="sub6")
    sub7 = models.CharField(_("Subject 7"), max_length=50, blank=True, null=True)
    tec7 = models.ForeignKey(TeachersInfoModel, on_delete=models.DO_NOTHING, null=True, blank=True, related_name="sub7")
    sub8 = models.CharField(_("Subject 8"), max_length=50, blank=True, null=True)
    tec8 = models.ForeignKey(TeachersInfoModel, on_delete=models.DO_NOTHING, null=True, blank=True, related_name="sub8")
    sub9 = models.CharField(_("Subject 9"), max_length=50, blank=True, null=True)
    tec9 = models.ForeignKey(TeachersInfoModel, on_delete=models.DO_NOTHING, null=True, blank=True, related_name="sub9")
    sub10 = models.CharField(_("Subject 10"), max_length=50, blank=True, null=True)
    tec10 = models.ForeignKey(
        TeachersInfoModel, on_delete=models.DO_NOTHING, null=True, blank=True, related_name="sub10"
    )
    sub11 = models.CharField(_("Subject 11"), max_length=50, blank=True, null=True)
    tec11 = models.ForeignKey(
        TeachersInfoModel, on_delete=models.DO_NOTHING, null=True, blank=True, related_name="sub11"
    )
    sub12 = models.CharField(_("Subject 12"), max_length=50, blank=True, null=True)
    tec12 = models.ForeignKey(
        TeachersInfoModel, on_delete=models.DO_NOTHING, null=True, blank=True, related_name="sub12"
    )

    def __str__(self):
        return self.name

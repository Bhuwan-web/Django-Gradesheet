from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class CourseModel(models.Model):
    name = models.CharField(_("Course Name"), max_length=50)
    grade = models.IntegerField(_("Grade"))
    sub1 = models.CharField(_("Subject 1"), max_length=50, blank=True, null=True)
    sub2 = models.CharField(_("Subject 2"), max_length=50, blank=True, null=True)
    sub3 = models.CharField(_("Subject 3"), max_length=50, blank=True, null=True)
    sub4 = models.CharField(_("Subject 4"), max_length=50, blank=True, null=True)
    sub5 = models.CharField(_("Subject 5"), max_length=50, blank=True, null=True)
    sub6 = models.CharField(_("Subject 6"), max_length=50, blank=True, null=True)
    sub7 = models.CharField(_("Subject 7"), max_length=50, blank=True, null=True)
    sub8 = models.CharField(_("Subject 8"), max_length=50, blank=True, null=True)
    sub9 = models.CharField(_("Subject 9"), max_length=50, blank=True, null=True)
    sub10 = models.CharField(_("Subject 10"), max_length=50, blank=True, null=True)
    sub11 = models.CharField(_("Subject 11"), max_length=50, blank=True, null=True)
    sub12 = models.CharField(_("Subject 12"), max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name

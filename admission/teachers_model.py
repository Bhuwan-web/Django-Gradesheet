from django.db import models
from django.db.models.fields import CharField
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField


class TeachersInfoModel(models.Model):
    f_name = models.CharField(_("First Name"), max_length=150)
    m_name = models.CharField(_("Middle Name"), max_length=150, null=True, blank=True)
    l_name = models.CharField(_("Last Name"), max_length=150)
    contact_no = CharField(_("Contact Number"), max_length=15, default="+977")
    email = models.EmailField(_("Email Address"), max_length=254, unique=True)
    short_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.short_name} {self.email}" or f"{self.f_name} {self.l_name} {self.email}"

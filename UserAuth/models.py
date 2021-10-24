from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Login(models.Model):
    email=models.EmailField(_("Email Address"), max_length=254,null=True)
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)


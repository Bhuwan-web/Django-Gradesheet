
# /////////////////////////////Custom User Model//////////////////////////////////////////////

from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser,PermissionsMixin
)
# from django.utils.translation import gettext_lazy as _



class CustomBaseUserManager(BaseUserManager):
    def create_user(self, email,role, password=None,**other_fields):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            role=role,
            **other_fields
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email,role, password=None,**other_fileds):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        other_fileds.setdefault("is_superuser",True)
        other_fileds.setdefault('is_active',True)
        user = self.create_user(
            email=email,
            password=password,
            role=role,
            **other_fileds
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


    
class User(AbstractBaseUser,PermissionsMixin):
    user_roles=(
        ("Teacher","Teacher"),
        ("Student","Student"),
        ("Parents","Parents"),
        ("Admin","Admin")
    )
    email = models.EmailField(
    verbose_name='email address',
    max_length=255,
    unique=True,
)
    username=models.CharField(max_length=150,unique=True)
    first_name=models.CharField(max_length=50,blank=True)
    last_name=models.CharField(max_length=50,blank=True)
    date_of_birth=models.DateField(blank=True,null=True)
    role=models.CharField(max_length=30,choices=user_roles,default="Student")
    about=models.TextField(max_length=500,blank=True)
    is_active=models.BooleanField(default=False)
    is_admin=models.BooleanField(default=False)


    objects=CustomBaseUserManager()
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=["role"]

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
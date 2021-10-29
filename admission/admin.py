from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


from admission.forms import UserAdmissionForm
from .models import UserInfo, StudentInfo, ParentsInfo, UserAdmission

# Register your models here.
class CustomUserInfoAdmin(admin.ModelAdmin):
    list_display = ("f_name", "date_of_birth", "address")
    search_fields = ("f_name", "address")
    list_per_page = 20


class CustomUserAdmissionAdmin(admin.ModelAdmin):
    list_display = ("basic_info", "student_info", "parents_info")


admin.site.register(UserInfo, CustomUserInfoAdmin)

admin.site.register([StudentInfo, ParentsInfo])
admin.site.register(UserAdmission, CustomUserAdmissionAdmin)

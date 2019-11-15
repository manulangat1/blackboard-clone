from django.contrib import admin

# Register your models here.
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from .forms import UserCreationForm, UserChangeForm
from .models import User,Student,Assignment,GradedAssignment,Question,Choice

class UserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    list_display = ['username', 'is_student', 'is_teacher']
    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('is_student', 'is_teacher')}),
    ) #this will allow to change these fields in admin module


admin.site.unregister(Group)
admin.site.register(User, UserAdmin)
admin.site.register(Assignment)
admin.site.register(GradedAssignment)
admin.site.register(Question)
admin.site.register(Choice)
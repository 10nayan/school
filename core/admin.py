from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import (
    UserProfile, SchoolClass, Student, Parent, ParentStudent,
    Department, Subject, Teacher, TeacherSubject, Staff, User
)

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ['email', 'username', 'role', 'is_active', 'first_name', 'last_name']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('username', 'role')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Important dates', {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'first_name', 'last_name', 'middle_name', 'role', 'password1', 'password2', 'is_active', 'is_staff', 'is_superuser'),
        }),
    )
    search_fields = ['username', 'email']
    ordering = ('email',)
    filter_horizontal = []  # Remove references to groups and user_permissions

# Admin class for UserProfile
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_no', 'address', 'created_at')
    search_fields = ('user__username', 'phone_no')
    ordering = ('user__username',)

# Admin class for SchoolClass
class SchoolClassAdmin(admin.ModelAdmin):
    list_display = ('name', 'section')
    search_fields = ('name', 'section')
    ordering = ('name',)

# Admin class for Student
class StudentAdmin(admin.ModelAdmin):
    list_display = ('user', 'class_assigned', 'enrollment_date', 'date_of_birth')
    search_fields = ('user__username', 'class_assigned__name')
    list_filter = ('class_assigned', 'enrollment_date')
    ordering = ('user__username',)

# Admin class for Parent
class ParentAdmin(admin.ModelAdmin):
    list_display = ('user',)
    search_fields = ('user__username',)
    ordering = ('user__username',)

# Admin class for ParentStudent
class ParentStudentAdmin(admin.ModelAdmin):
    list_display = ('parent', 'student')
    search_fields = ('parent__user__username', 'student__user__username')

# Admin class for Department
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)

# Admin class for Subject
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'department')
    search_fields = ('name', 'code')
    list_filter = ('department',)
    ordering = ('name',)

# Admin class for Teacher
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('user', 'department', 'joining_date', 'qualifications')
    search_fields = ('user__username', 'department__name')
    list_filter = ('department', 'joining_date')
    ordering = ('user__username',)

# Admin class for TeacherSubject
class TeacherSubjectAdmin(admin.ModelAdmin):
    list_display = ('teacher', 'subject')
    search_fields = ('teacher__user__username', 'subject__name')

# Admin class for Staff
class StaffAdmin(admin.ModelAdmin):
    list_display = ('user',)
    search_fields = ('user__username',)
    ordering = ('user__username',)

admin.site.register(User, CustomUserAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(SchoolClass, SchoolClassAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Parent, ParentAdmin)
admin.site.register(ParentStudent, ParentStudentAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(TeacherSubject, TeacherSubjectAdmin)
admin.site.register(Staff, StaffAdmin)
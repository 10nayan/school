from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        """Create a user with username, email and passsword"""
        if not email:
            raise ValueError("Email is a mandatory field")
        if not username:
            raise ValueError("Username is a mandatory field")
        
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, password, email, **extra_fields):
        """Create a superuser with role admin"""
        extra_fields.setdefault('role', 'admin')
        extra_fields.setdefault('is_stuff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=255, unique=True)
    first_name = models.CharField(max_length=30, null=False, blank=False)
    middle_name = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=30, null=False, blank=True)
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=30)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return f'{self.email}'


class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='profile'
    )
    phone_no = models.CharField(max_length=10, null=True, blank=True)
    address = models.TextField(blank=True, null=True)
    created_at = models.DateField(default=timezone.now)

    def __str__(self):
        return f'{self.user.username}'


class SchoolClass(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False)
    section = models.CharField(max_length=30, null=True, blank=True)
    subjects = models.ManyToManyField('Subject', related_name='classes')

    def __str__(self):
        return f'{self.name}-{self.section}'


class Student(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='student'
    )
    class_assigned = models.ForeignKey(
        'SchoolClass',
        on_delete=models.SET_NULL,
        null=True,
        related_name='student'
    )
    enrollment_date = models.DateTimeField(default=timezone.now)
    date_of_birth = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'Student: {self.user.first_name} {self.user.last_name} - {self.class_assigned}'


class Parent(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='parent'
    )

    def __str__(self):
        return f'Parent: {self.user.first_name} {self.user.last_name}'
    

class ParentStudent(models.Model):
    parent = models.ForeignKey('Parent', on_delete=models.CASCADE)
    student = models.ForeignKey('Student', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('parent', 'student')

    def __str__(self):
        return f'Parent {self.parent.user.username} - Student {self.student.user.username}'
    

class Department(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.name}'
    

class Subject(models.Model):
    name = models.CharField(max_length=60, null=False, blank=False)
    code = models.CharField(max_length=10, null=True, blank=True)
    department = models.ForeignKey('Department', on_delete=models.SET_NULL, null=True, related_name='subject_department')

    def __str__(self):
        return f'Subject {self.code} {self.name}'


class Teacher(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='teacher'
    )
    department = models.ForeignKey('Department', on_delete=models.SET_NULL, null=True, related_name='teacher_department')
    joining_date = models.DateField(auto_now_add=True)
    qualifications = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'Teacher: {self.user.first_name} {self.user.last_name}'
    

class TeacherSubject(models.Model):
    teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE)
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('teacher', 'subject')

    def __str__(self):
        return f'Teacher {self.teacher.user.username} - Subject {self.subject.name}'
    

class Staff(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='staff'
    )

    def __str__(self):
        return f'Staff: {self.user.first_name} {self.user.last_name}'
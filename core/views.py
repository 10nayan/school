from django.db.models.manager import BaseManager
from django.shortcuts import render
from rest_framework import viewsets
from .models import Department, SchoolClass, Subject
from .serializers import DepartmentSerializer, SchoolClassSerializer, SubjectSerializer


class DepartmentViewset(viewsets.ModelViewSet):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()


class SubjectViewset(viewsets.ModelViewSet):
    serializer_class = SubjectSerializer
    queryset: BaseManager[Subject] = Subject.objects.all()


class SchoolClassViewset(viewsets.ModelViewSet):
    serializer_class = SchoolClassSerializer
    queryset = SchoolClass.objects.all()

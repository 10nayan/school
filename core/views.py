from rest_framework import viewsets, status, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from .models import Department, SchoolClass, Subject
from .serializers import DepartmentSerializer, SchoolClassSerializer, SubjectSerializer
from .services import department_service, subject_service, class_service
from .pydantic import (
    DepartmentCreate, DepartmentUpdate,
    SubjectCreate, SubjectUpdate,
    SchoolClassCreate, SchoolClassUpdate
)


class DepartmentViewset(viewsets.ModelViewSet):
    serializer_class = DepartmentSerializer
    queryset = department_service.get_all_departments()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['name']
    search_fields = ['name']
    ordering_fields = ['name', 'id']
    ordering = ['name']  # default ordering

    def create(self, request, *args, **kwargs):
        data = DepartmentCreate(**request.data)
        department = department_service.create_department(data)
        serializer = self.get_serializer(department)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        data = DepartmentUpdate(**request.data)
        department = department_service.update_department(kwargs['pk'], data)
        serializer = self.get_serializer(department)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        department_service.delete_department(kwargs['pk'])
        return Response(status=status.HTTP_204_NO_CONTENT)


class SubjectViewset(viewsets.ModelViewSet):
    serializer_class = SubjectSerializer
    queryset = subject_service.get_all_subjects()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['name', 'code', 'department']
    search_fields = ['name', 'code']
    ordering_fields = ['name', 'code', 'id']
    ordering = ['name']  # default ordering

    def create(self, request, *args, **kwargs):
        data = SubjectCreate(**request.data)
        subject = subject_service.create_subject(data)
        serializer = self.get_serializer(subject)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        data = SubjectUpdate(**request.data)
        subject = subject_service.update_subject(kwargs['pk'], data)
        serializer = self.get_serializer(subject)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        subject_service.delete_subject(kwargs['pk'])
        return Response(status=status.HTTP_204_NO_CONTENT)


class SchoolClassViewset(viewsets.ModelViewSet):
    serializer_class = SchoolClassSerializer
    queryset = class_service.get_all_classes()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['name', 'section', 'subjects']
    search_fields = ['name', 'section']
    ordering_fields = ['name', 'section', 'id']
    ordering = ['name', 'section']  # default ordering

    def create(self, request, *args, **kwargs):
        data = SchoolClassCreate(**request.data)
        school_class = class_service.create_class(data)
        serializer = self.get_serializer(school_class)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        data = SchoolClassUpdate(**request.data)
        school_class = class_service.update_class(kwargs['pk'], data)
        serializer = self.get_serializer(school_class)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        class_service.delete_class(kwargs['pk'])
        return Response(status=status.HTTP_204_NO_CONTENT)

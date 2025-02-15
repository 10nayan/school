from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SchoolClassViewset, SubjectViewset, DepartmentViewset

router = DefaultRouter()
router.register(r'subject', SubjectViewset)
router.register(r'department', DepartmentViewset)
router.register(r'class', SchoolClassViewset)

urlpatterns = [
    path('', include(router.urls)),
]
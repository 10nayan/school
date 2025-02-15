from typing import List
from django.db.models.manager import BaseManager
from core.models import Subject
from core.serializers import SubjectSerializer
from core.pydantic import SubjectCreate, SubjectUpdate

def get_all_subjects() -> BaseManager[Subject]:
    """
    Get all subjects from the database
    """
    return Subject.objects.all()

def get_subject_by_id(subject_id: int) -> Subject:
    """
    Get a subject by its ID
    """
    return Subject.objects.get(id=subject_id)

def create_subject(data: SubjectCreate) -> Subject:
    """
    Create a new subject
    Args:
        data: Validated subject data
    """
    subject_dict = data.model_dump()
    serializer = SubjectSerializer(data=subject_dict)
    if serializer.is_valid(raise_exception=True):
        return serializer.save()

def update_subject(subject_id: int, data: SubjectUpdate) -> Subject:
    """
    Update an existing subject
    Args:
        subject_id: ID of the subject to update
        data: Validated update data
    """
    subject = get_subject_by_id(subject_id)
    subject_dict = data.model_dump(exclude_unset=True)
    serializer = SubjectSerializer(subject, data=subject_dict, partial=True)
    if serializer.is_valid(raise_exception=True):
        return serializer.save()

def delete_subject(subject_id: int) -> None:
    """
    Delete a subject
    """
    subject = get_subject_by_id(subject_id)
    subject.delete()

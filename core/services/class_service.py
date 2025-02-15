from typing import List
from core.models import SchoolClass, Subject
from core.serializers import SchoolClassSerializer
from core.pydantic import SchoolClassCreate, SchoolClassUpdate

class SchoolClassService:
    @staticmethod
    def get_all_classes() -> List[SchoolClass]:
        """
        Get all school classes from the database
        """
        return SchoolClass.objects.all()

    @staticmethod
    def get_class_by_id(class_id: int) -> SchoolClass:
        """
        Get a school class by its ID
        """
        return SchoolClass.objects.get(id=class_id)

    @staticmethod
    def create_class(data: SchoolClassCreate) -> SchoolClass:
        """
        Create a new school class
        Args:
            data: Validated school class data
        """
        class_dict = data.model_dump(exclude={'subject_ids'})
        serializer = SchoolClassSerializer(data=class_dict)
        if serializer.is_valid(raise_exception=True):
            school_class = serializer.save()
            
            # Handle many-to-many relationship with subjects
            if data.subject_ids:
                subjects = Subject.objects.filter(id__in=data.subject_ids)
                school_class.subjects.set(subjects)
            
            return school_class

    @staticmethod
    def update_class(class_id: int, data: SchoolClassUpdate) -> SchoolClass:
        """
        Update an existing school class
        Args:
            class_id: ID of the school class to update
            data: Validated update data
        """
        school_class = SchoolClassService.get_class_by_id(class_id)
        class_dict = data.model_dump(exclude={'subject_ids'}, exclude_unset=True)
        serializer = SchoolClassSerializer(school_class, data=class_dict, partial=True)
        if serializer.is_valid(raise_exception=True):
            school_class = serializer.save()
            
            # Handle many-to-many relationship with subjects if provided
            if data.subject_ids is not None:
                subjects = Subject.objects.filter(id__in=data.subject_ids)
                school_class.subjects.set(subjects)
            
            return school_class

    @staticmethod
    def delete_class(class_id: int) -> None:
        """
        Delete a school class
        """
        school_class = SchoolClassService.get_class_by_id(class_id)
        school_class.delete()

from typing import List
from core.models import Department
from core.serializers import DepartmentSerializer
from core.pydantic import DepartmentCreate, DepartmentUpdate

def get_all_departments() -> List[Department]:
    """
    Get all departments from the database
    """
    return Department.objects.all()

def get_department_by_id(department_id: int) -> Department:
    """
    Get a department by its ID
    """
    return Department.objects.get(id=department_id)

def create_department(data: DepartmentCreate) -> Department:
    """
    Create a new department
    Args:
        data: Validated department data
    """
    department_dict = data.model_dump()
    serializer = DepartmentSerializer(data=department_dict)
    if serializer.is_valid(raise_exception=True):
        return serializer.save()

def update_department(department_id: int, data: DepartmentUpdate) -> Department:
    """
    Update an existing department
    Args:
        department_id: ID of the department to update
        data: Validated update data
    """
    department = get_department_by_id(department_id)
    department_dict = data.model_dump(exclude_unset=True)
    serializer = DepartmentSerializer(department, data=department_dict, partial=True)
    if serializer.is_valid(raise_exception=True):
        return serializer.save()

def delete_department(department_id: int) -> None:
    """
    Delete a department
    """
    department = get_department_by_id(department_id)
    department.delete()

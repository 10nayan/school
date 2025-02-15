from typing import Optional
from pydantic import BaseModel


class DepartmentBase(BaseModel):
    """Base model with common attributes"""
    name: str

class DepartmentCreate(DepartmentBase):
    """Create model requires all fields"""
    pass

class DepartmentUpdate(BaseModel):
    """Update model makes all fields optional"""
    name: Optional[str] = None


class SubjectBase(BaseModel):
    """Base model with common attributes"""
    name: str
    code: Optional[str] = None
    department_id: Optional[int] = None

class SubjectCreate(SubjectBase):
    """Create model requires name field"""
    pass

class SubjectUpdate(BaseModel):
    """Update model makes all fields optional"""
    name: Optional[str] = None
    code: Optional[str] = None
    department_id: Optional[int] = None


class SchoolClassBase(BaseModel):
    """Base model with common attributes"""
    name: str
    section: Optional[str] = None
    subject_ids: Optional[list[int]] = None

class SchoolClassCreate(SchoolClassBase):
    """Create model requires name field"""
    pass

class SchoolClassUpdate(BaseModel):
    """Update model makes all fields optional"""
    name: Optional[str] = None
    section: Optional[str] = None
    subject_ids: Optional[list[int]] = None

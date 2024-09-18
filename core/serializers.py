from rest_framework import serializers
from .models import Subject, SchoolClass, Department


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ["name"]


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ["id", "name", "code", "department"]


class SchoolClassSerializer(serializers.ModelSerializer):
    subjects = SubjectSerializer(many=True)

    class Meta:
        model = SchoolClass
        fields = ["id", "name", "section", "subjects"]
    
    def create(self, validated_data):
        subjects_data = validated_data.pop('subjects', [])
        school_class = SchoolClass.objects.create(**validated_data)

        # Handling the creation or linking of subjects
        for subject_data in subjects_data:
            subject, created = Subject.objects.get_or_create(**subject_data)
            school_class.subjects.add(subject)

        return school_class
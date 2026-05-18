from rest_framework import serializers
from students.models import Student
from Employees.models import Employee
class StudentSerializer(serializers.ModelSerializer):
    class Meta: # The Meta class is a nested class that provides metadata to the serializer. It tells the serializer which model to use and which fields to include in the serialization process.
        model = Student
        fields = '__all__' # this means we want to serialize all the fields of the Student model. You can also specify specific fields like fields = ['name', 'age', 'grade'] if you only want to serialize certain fields.

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
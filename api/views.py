#from django.http import JsonResponse
#from django.shortcuts import render

from students.models import Student
from .serializers import StudentSerializer, EmployeeSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from Employees.models import Employee
from django.http import Http404
from rest_framework import mixins, generics
# Create your views here.

@api_view(['GET','POST']) # This decorator is used to specify that the studentsView function should only handle defined requests. If a different type of request is made to this view, it will return a 405 Method Not Allowed response.
def studentsView(request): 
   # students = list(Student.objects.all().values()) # .values() returns a QuerySet of dictionaries instead of model instances. Each dictionary represents a student with its fields as key-value pairs.
   # return JsonResponse(students, safe=False)       # Safe = False allows us to return a list of objects instead of a dictionary. 
                                                    #By default, JsonResponse expects a dictionary, so we set safe to False to allow for a list.
   # function based view
   if request.method == 'GET':
       students = Student.objects.all() # This retrieves all the Student objects from the database and returns a QuerySet.
       serializer = StudentSerializer(students, many=True) # This creates an instance of the StudentSerializer and passes the students QuerySet to it. The many=True argument tells the serializer that we are serializing a list of objects.
       return Response(serializer.data, status=status.HTTP_200_OK) # This returns a Response object containing the serialized data. The serializer.data attribute contains the serialized representation of the students QuerySet, which is typically a list of dictionaries representing each student.
   
   elif request.method == 'POST':
       serializer = StudentSerializer(data=request.data)
       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status=status.HTTP_201_CREATED)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT','DELETE'])
def studentsDetailView(request, pk):
      try:
          student = Student.objects.get(pk=pk)
      except Student.DoesNotExist:
          return Response(status=status.HTTP_404_NOT_FOUND)
      if request.method == 'GET':
          serializer = StudentSerializer(student)
          return Response(serializer.data, status=status.HTTP_200_OK)
      
      elif request.method == 'PUT':
          serializer = StudentSerializer(student, data=request.data) # if want to upidate the data of an existing student, we need to pass the instance of the student we want to update as the first argument to the serializer, and the new data as the second argument. This way, the serializer knows which student to update with the new data.
          if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK) 
          else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
      elif request.method == 'DELETE':
          student.delete()
          return Response(status=status.HTTP_204_NO_CONTENT)

# Class based views

# class Employees(APIView):
#     def get(self, request):
#         employees = Employee.objects.all()
#         serializer = EmployeeSerializer(employees, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     def post(self, request):
#         serializer = EmployeeSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# # Primary key based operations

# class EmployeeDetail(APIView):
#     def get_object(self, pk):
#         try:
#             return Employee.objects.get(pk=pk)
#         except Employee.DoesNotExist:
#             raise Http404

#     def get(self,request, pk):
#         employee = self.get_object(pk)
#         serializer = EmployeeSerializer(employee)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def put(self, request, pk):
#         employee = self.get_object(pk)
#         serializer = EmployeeSerializer(employee, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk):
#         employee = self.get_object(pk)
#         employee.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# Using mixins and generics from same Employee views

class Employees(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get(self, request):
        return self.list(request)
    def post(self, request):
        return self.create(request)

# PK related opertions
class EmployeeDetail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk)
    
    def put(self, request, pk):
        return self.update(request, pk)

    def delete(self, request, pk):
        return self.destroy(request, pk)
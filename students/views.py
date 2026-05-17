from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
def students(request):
    student ={
        'name': 'John Doe',
        'age': 20,
        'grade': 'A'
    }
    return JsonResponse(student)
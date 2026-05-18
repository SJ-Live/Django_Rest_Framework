from django.urls import include, path

from . import views

urlpatterns = [
    path('students/', views.studentsView),
    path('students/<int:pk>', views.studentsDetailView),

    path('employees/', views.Employees.as_view()), # This as_view() means we are using class based views. It converts the Employees class into a view that can handle HTTP requests.
    path('employees/<int:pk>', views.EmployeeDetail.as_view()),
]

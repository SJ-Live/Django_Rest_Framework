from django.urls import include, path

from . import views

urlpatterns = [
    path('students/', views.studentsView),
    path('students/<int:pk>', views.studentsDetailView),
]

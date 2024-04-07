from django.urls import path
from . import views
# from django import views

urlpatterns = [
    path('automatic/<uuid:submission_id>/', views.automatic_grading, name = 'automatic_grading'),
    path('',views.plagiarism_checker2, name = 'plagiarism_checker2'),
]

from django.urls import path

from . import views

app_name = 'students'

urlpatterns = [
    path('<int:pk>/edit/', views.student, name='student_edit'),
    path('<int:pk>/delete/', views.student_delete, name='student_delete'),
    path('list/', views.students_list, name='students_list'),
    path('', views.student, name='student_create'),
]

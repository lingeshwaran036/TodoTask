from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('task/add/', views.add_task, name='add_task'),
    path('marked/<int:task_id>', views.mark_as_complete, name='marked'),
    path('task/edit/<int:task_id>', views.edit_task, name='edit_task'),
    path('task/delete/<int:task_id>', views.delete_task, name='delete_task'),
    path('logout/', views.logout, name='logout'),
]
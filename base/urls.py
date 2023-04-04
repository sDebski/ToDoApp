from django.urls import path
from . import views


urlpatterns = [
    path('', views.TaskList.as_view(), name='tasks'),
    path('tasks/<str:pk>/', views.TaskDetail.as_view(), name='task'),
    path('task-create/', views.TaskCreate.as_view(), name='task-create'),
    path('task-update/<str:pk>', views.TaskUpdate.as_view(), name='task-update'),
]

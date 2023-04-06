from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', views.RegisterPage.as_view(), name='register'),
    path('', views.TaskList.as_view(), name='tasks'),
    path('tasks/<str:pk>/', views.TaskDetail.as_view(), name='task'),
    path('task-create/', views.TaskCreate.as_view(), name='task-create'),
    path('task-update/<str:pk>', views.TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<str:pk>', views.TaskDelete.as_view(), name='task-delete'),
]

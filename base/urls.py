from django.urls import path
from django.contrib.auth.views import LogoutView

from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete, LoginView, RegisterView, TaskReorder

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('create/task/', TaskCreate.as_view(), name='create'),
    path('update/task/<int:pk>/', TaskUpdate.as_view(), name='update'),
    path('delete/task/<int:pk>/', TaskDelete.as_view(), name='delete'),
    path('reorder/task/', TaskReorder.as_view(), name='reorder'),
]

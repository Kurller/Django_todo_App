from django.urls import path
from . import views

urlpatterns = [
    path("",views.task_list,name = 'task-list'),
    path("task/<int:pk>/delete",views.task_delete,name = 'task-delete'),
    path("task/<int:pk>/dupdate",views.task_update,name = 'task-update')
]


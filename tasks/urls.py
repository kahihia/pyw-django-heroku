from django.urls import path

from . import views
from django.views.generic import TemplateView
app_name = "tasks"

urlpatterns = [
    path("iframe/", TemplateView.as_view(template_name='tasks/details.html'), name='iframe'),
    path("", TemplateView.as_view(template_name='tasks/create.html')),
    path("create/", views.TaskCreateView.as_view(), name="create"),
    path("add-task/", views.add_task, name="api-add-task"),
    path("complete/<int:uid>", views.complete_task, name="complete"),
    path("delete/<int:uid>", views.delete_task, name="delete"),
    path("details/<int:pk>", views.TaskDetailsView.as_view(), name="details"),
    path("edit/<int:pk>", views.TaskEditView.as_view(), name="edit"),
    path("export/", views.TaskExportView.as_view(), name="export"),
]

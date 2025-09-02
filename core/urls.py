from django.urls import path
from .views import (
    TaskCreateView,
    TaskListView, TaskUpdateView,
    TaskDeleteView, TagListView, TagCreateView,
    TagUpdateView, TagDeleteView, perform_action)

urlpatterns = [
    path("", TaskListView.as_view(), name="task_list"),
    path("create/", TaskCreateView.as_view(), name="task_create"),
    path("update/<int:pk>/", TaskUpdateView.as_view(), name="task_update"),
    path("delete/<int:pk>/", TaskDeleteView.as_view(), name="task_delete"),
    path("tags/", TagListView.as_view(), name="tag_list"),
    path("tags/create/", TagCreateView.as_view(), name="tag_create"),
    path("tags/update/<int:pk>/", TagUpdateView.as_view(), name="tag_update"),
    path("tags/delete/<int:pk>/", TagDeleteView.as_view(), name="tag_delete"),
    path("tasks/<int:pk>/perform_action/", perform_action, name="task_perform_action"),
]

app_name = "core"
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic

from core.models import Tag, Task


class TaskListView(generic.ListView):
    model = Task
    queryset = Task.objects.all()
    context_object_name = 'task_list'

class TaskCreateView(generic.CreateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('core:task_list')

class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('core:task_list')

class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy('core:task_list')


class TagListView(generic.ListView):
    model = Tag
    queryset = Tag.objects.all()
    context_object_name = 'tag_list'

class TagCreateView(generic.CreateView):
    model = Tag
    fields = '__all__'
    success_url = reverse_lazy('core:tag_list')

class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = '__all__'
    success_url = reverse_lazy('core:tag_list')

class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy('core:tag_list')


def perform_action(request, pk) -> HttpResponse:
    task = Task.objects.get(id=pk)
    if task.task_done:
        task.task_done = False
    else:
        task.task_done = True
    task.save()

    return HttpResponseRedirect(reverse_lazy('core:task_list'))


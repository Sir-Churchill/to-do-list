from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Task(models.Model):
    content = models.CharField(max_length=255)
    datetime = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    task_done = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, related_name='tasks')

    class Meta:
        ordering = ['task_done', '-datetime']

    def __str__(self):
        return self.content

    @property
    def status_text(self):
        return "Done" if self.task_done else "Not Done"

    @property
    def status_class(self):
        return "color: green" if self.task_done else "color: red"
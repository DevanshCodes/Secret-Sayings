from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Todo(models.Model):
    text = models.CharField(max_length=100)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.text

class Todo_likes(models.Model):
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
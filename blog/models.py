from django.db import models
from django.contrib.auth.models import User

class Content(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
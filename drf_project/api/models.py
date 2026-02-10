from django.db import models
from django.contrib.auth.models import User

class Snippet(models.Model):
    title = models.CharField(max_length=100, blank=True)
    code = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, related_name='snippets', on_delete=models.CASCADE)

    def __str__(self):
        return self.title or f"Snippet {self.pk}"
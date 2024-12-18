from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class SharedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Post(SharedModel):
    title = models.CharField(max_length=200)
    body = models.TextField()
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

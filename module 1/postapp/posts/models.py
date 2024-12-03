from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="posts")
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="images/", null=True)

    def __str__(self):
        return str(self.description)

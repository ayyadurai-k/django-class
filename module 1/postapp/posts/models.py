from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.name}-{self.id}"

class Post(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="posts") 
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="images/", null=True)
    category = models.ManyToManyField(
        Category, related_name="posts",blank=True) 
    def __str__(self):
        return str(self.description)

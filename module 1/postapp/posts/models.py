from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="images/", null=True)

    def __str__(self):
        return str(self.description)
    
    
    
    

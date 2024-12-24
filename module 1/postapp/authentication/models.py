from django.db import models
from django.contrib.auth.models import User

#ONE TO ONE FIELD 

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile")
    bio = models.TextField()
    image = models.ImageField(upload_to="profile-images/", null=True)
    
    def __str__(self):
        return str(self.user)
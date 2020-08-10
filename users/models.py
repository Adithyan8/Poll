from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Creator(models.Model):
    name = models.OneToOneField(User,on_delete=models.CASCADE)
    profilepic = models.ImageField(upload_to="profile_pictures",height_field=300,width_field=300)

    def __str__(self):
        return f'hello'

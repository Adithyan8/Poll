from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User
from django.utils import timezone

class Question(models.Model):
    pollq = models.CharField(max_length=100)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    date_posted = models.DateField(default=timezone.now)
    option1=models.CharField(max_length=30)
    option2=models.CharField(max_length=30)
    option3=models.CharField(max_length=30)
    option1votes = models.IntegerField(default=0)
    option2votes = models.IntegerField(default=0)
    option3votes = models.IntegerField(default=0)
    def get_absolute_url(self):
        return reverse("qdetail",kwargs={'pk':self.pk})
    def __str__(self):
        return self.pollq

""" class OptionVote(models.Model):
    pollq = models.ForeignKey(Question,on_delete=models.CASCADE)
    option = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.option """

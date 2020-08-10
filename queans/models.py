from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User

class Question(models.Model):
    pollq = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse("qdetail",kwargs={'pk':self.pk})
    def __str__(self):
        return self.pollq

class OptionVote(models.Model):
    pollq = models.ForeignKey(Question,on_delete=models.CASCADE)
    option = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.option

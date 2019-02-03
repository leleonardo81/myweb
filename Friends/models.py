from django.db import models
from django.contrib.auth.models import User


class Friend(models.Model):
    username = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    gender = models.TextField(choices=(('Male',"Male"),('Female', "Female")))
    birthplace = models.CharField(max_length=50)
    birthday = models.DateField()
    line = models.CharField(max_length=50)
    desc = models.TextField(default="")
 
    def __str__(self):
        return "{} - {}".format(self.username, self.name)
    
from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=150,null=True)
    content = models.TextField()
    author = models.CharField(max_length=150,null=True)
    timeStamp = models.DateTimeField(default=now)
    addressdlug=models.CharField(max_length=150)
    def __str__(self):
        return f'Blog about {self.title} by {self.author}' 


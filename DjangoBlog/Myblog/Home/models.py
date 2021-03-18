from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=150)
    phone = models.CharField(max_length = 14)
    content = models.TextField()
    email = models.CharField(max_length=150)
    timeStamp = models.DateTimeField(auto_now_add=True,blank=True)

    def __str__(self):
        return f'Message from {self.name}'
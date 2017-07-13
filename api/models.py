from django.db import models

# Create your models here.

class User(models.Model):
    name     = models.CharField(max_length=100)
    email    = models.CharField(max_length=100)
    password = models.TextField()
    gender   = models.CharField(max_length=6)
    def __str__(self):
        return self.name

class Message(models.Model):
    from_user = models.ForeignKey(User, related_name='to_user')
    to_user   = models.ForeignKey(User, related_name='from_user')
    title     = models.CharField(max_length=100)
    message   = models.CharField(max_length=1000)
    sentat    = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

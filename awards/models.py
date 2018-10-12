from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=20)
    bio = models.TextField(max_length=200, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)

class Post(models.Model):

    image = models.ImageField()
    image_name= models.CharField(max_length=10)
    user = models.ForeignKey(User, related_name='posted_by', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date']
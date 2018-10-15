from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name="profile")
    bio = models.CharField(max_length=256)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, default="media/jVr43h8.png")

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    @classmethod
    def get_all(cls):
        profile = cls.objects.all()
        return profile


class Project(models.Model):

    image = models.ImageField(upload_to='images/')
    site_link= models.CharField(max_length=100)
    site_description = models.CharField(max_length=100)
    user = models.ForeignKey(User, related_name='posted_by', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date']

    @classmethod
    def get_all(cls):
        projects = cls.objects.all()
        return projects

    @classmethod
    def search_project(cls,search_term):
        projects = cls.objects.filter(site_description__icontains=search_term)
        return projects

from django.test import TestCase
from .models import *
import datetime as dt

# Create your tests here.
class ProfileTestClass(TestCase):

    def setUp(self):
        self.Pro= Profile(name = 'Dan', bio='Made with love')

# Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.Pro,Profile))

    def test_save_method(self):
        self.Pro.save_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile) > 0)

    def test_data(self):
        self.assertTrue(self.Pro.name,"test")

    def test_delete(self):
        post = Profile.objects.filter(id=1)
        post.delete()
        posts = Profile.objects.all()
        self.assertTrue(len(posts)==0)

    def test_get_post_by_id(self):
        self.Pro.save()
        posts = Profile.objects.get(id=1)
        self.assertTrue(posts.name,'kol')

class ProjectsTestClass(TestCase):

    def setUp(self):
        self.Pro= Projects(name = 'dan', description='Made with love')

# Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.Pro,Projects))

    def test_save_method(self):
        self.Pro.save_project()
        project = Projects.objects.all()
        self.assertTrue(len(project) > 0)

    def test_data(self):
        self.assertTrue(self.Pro.name,"test")

    def test_delete(self):
        post = Projects.objects.filter(id=1)
        post.delete()
        posts = Projects.objects.all()
        self.assertTrue(len(posts)==0)

    def test_get_post_by_id(self):
        self.Pro.save()
        posts = Projects.objects.get(id=1)
        self.assertTrue(posts.name,'kol')
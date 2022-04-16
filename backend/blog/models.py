from django.db import models
from django.forms import SlugField
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=250,blank=True)
    Slug = models.SlugField(blank=True)
    auther = models.ForeignKey(User, on_delete=models.CASCADE,blank=True)
    content = models.TextField(blank=True)
    publish = models.DateTimeField(default=timezone.now,blank=True)
    created = models.DateTimeField(auto_now_add=True,blank=True)
    updated = models.DateTimeField(auto_now=True,blank=True)
    status = models.BooleanField(default=False,blank=True)

    def __str__(self):
        return (self.title, self.auther, self.created)
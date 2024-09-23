from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class JobPosting(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    title = models.CharField(max_length=30, default="")
    pub_date = models.DateTimeField("date published" , default=timezone.now)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    content = models.TextField()


from django.contrib import admin

from .models import JobPosting, Category

# Register your models here.

admin.site.register(JobPosting)

admin.site.register(Category)
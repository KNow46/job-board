from django.urls import path

from . import views

app_name = "job_postings"
urlpatterns = [
    path("", views.JobListView.as_view(), name="job_postings"),
    path("create/", views.JobPostingCreateView.as_view(), name="create_posting"),
]
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import CreateView

from .models import JobPosting, Category


class JobListView(generic.ListView):
    model = JobPosting
    template_name = "job_postings/job_postings.html"
    context_object_name = 'job_postings_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        job_postings_list = context[self.context_object_name]


        unique_categories = JobPosting.objects.values_list('category__name', flat=True).distinct()
        context['unique_categories'] = unique_categories

        selected_category = self.request.GET.get('categoryy')
        if selected_category:
            job_postings_list = job_postings_list.filter(category__name=selected_category)

        context[self.context_object_name] = job_postings_list
        return context


class JobPostingCreateView(CreateView):
    model = JobPosting
    fields = ['title',  'category', 'content']
    #form_class = JobPostingForm
    template_name = 'job_postings/create_job_posting.html'
    success_url = reverse_lazy('job_postings:job_postings')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

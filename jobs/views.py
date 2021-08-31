from jobs.models import Job
from django.shortcuts import get_object_or_404, render


def home(request):
    jobs = Job.objects
    return render(request, 'jobs/home.html', {'jobs': jobs})


def detal(request, job_id):
    job_detail = get_object_or_404(Job, pk=job_id)
    return render(request, {'jobs/detail.html'})

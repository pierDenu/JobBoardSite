from django.shortcuts import render, redirect

from jobs.forms import JobForm
from jobs.models import Job


def create(request):
    form = JobForm()
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_job')
    return render(request, 'create_job.html', {"form": form})

def display_all(request):
    jobs = Job.objects.all()
    if request.method == 'GET':
        return render(request, 'display_all.html', {"jobs": jobs})


def display_one(request, job_id):
    job = Job.objects.get(id=job_id)
    if request.method == 'GET':
        return render(request, 'display_one.html', {"job": job})





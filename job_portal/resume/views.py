from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from .models import Resume
from .form import ResumeUpdateForm
from users.models import User


#update resume
def update_resume(request):
    resume = Resume.objects.get(user = request.user)
    if request.method == 'POST':
        form = ResumeUpdateForm(request.POST , request.FILES, instance=resume)
        if form.is_valid():
            var = form.save(commit = False)
            request.user.has_resume = True
            var.save()
            request.user.save()
            messages.info(request,'Your resume has been updated. You can now start applying to jobs')
            return redirect('dashboard')
        else:
            messages.warning(request,'Something went wrong')
    else:
        form = ResumeUpdateForm(instance=resume)
        context = {'form' : form}
        return render(request,'resume/update_resume.html',context)
    

#view resume details
def resume_details(request):
    resume = get_object_or_404(Resume, user=request.user)
    context = {'resume':resume}
    return render(request,'resume/resume_details.html',context)

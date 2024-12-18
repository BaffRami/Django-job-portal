from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import User
from .form import RegisterUserForm
from resume.models import Resume
from company.models import Company
from django.views.decorators.cache import never_cache

# registration for applicants
@never_cache
def register_applicant(request):
    if request.user.is_authenticated:
       return redirect('dashboard')
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.is_applicant = True
            var.username = var.email
            var.save()
            Resume.objects.create(user=var)
            messages.info(request, 'Your account has been successfully created')
            return redirect('login')
        else:
            messages.warning(request, 'Something went wrong')
            return redirect('register-applicant')
    else:
        form = RegisterUserForm()
        context = {'form': form}
        return render(request, 'users/register_applicant.html', context)

    

#registration for recruiters
@never_cache
def register_recruiter(request):
    if request.user.is_authenticated:
       return redirect('dashboard')
    if request.method == 'POST':
      form = RegisterUserForm(request.POST)
      if form.is_valid():
         var = form.save(commit=False)
         var.is_recruiter = True
         var.username = var.email
         var.save()
         Company.objects.create(user=var)
         messages.info(request, 'Your account has been succesfully created')
         return redirect('login')
      else:
         messages.warning(request, 'Something went wrong')
         return redirect('register-recruiter')
    else:
       form = RegisterUserForm()
       context = {'form': form}
       return render(request, 'users/register_recruiter.html', context)
    


#login users
@never_cache
def login_user(request):
   if request.user.is_authenticated:
      return redirect('dashboard')
   if request.method == 'POST':
      email = request.POST.get('email')
      password = request.POST.get('password')

      user = authenticate(request,username=email,password=password)
      if user is not None and user.is_active:
         login(request, user)
         return redirect('dashboard')
      else: 
         messages.warning(request, 'Somethings went wrong')
         return redirect('login')
   else:
      return render(request, 'users/login.html')
   

#logout users
def logout_user(request):
   logout(request)
   messages.info(request,'Your session has ended')
   return redirect ('login')
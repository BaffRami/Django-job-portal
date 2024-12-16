from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from .models import Company
from .form import UpdateCompanyForm
from users.models import User


#update company
def update_company(request):
    company = Company.objects.get(user=request.user)
    if request.method == 'POST':
        form = UpdateCompanyForm(request.POST, instance=company)
        if form.is_valid():
            var = form.save(commit=False)
            request.user.has_company = True
            var.save()
            request.user.save()
            messages.info(request,'Your company details have been updated. You can start creating job offers')
            return redirect('dashboard')
        else:
            messages.warning(request,'Something went wrong')
    else:
        form = UpdateCompanyForm(instance=company)
        context = {'form':form}
        return render(request,'company/update_company.html',context)
    

#view company details
def company_details(request):
    company = get_object_or_404(Company, user=request.user)
    context = {'company':company}
    return render(request,'company/company_details.html',context)



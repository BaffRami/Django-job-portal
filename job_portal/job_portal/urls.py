from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect

def redirect_to_register(request):
    return redirect('register-applicant')


urlpatterns = [
    path('admin/', admin.site.urls),  # Admin routes
    path('accounts/', include('users.urls')),  # User-related views under accounts
    path('dashboard/', include('dashboard.urls')),  # Dashboard routes
    path('company/',include('company.urls')), # Company routes
    path('resume/',include('resume.urls')), # Resume routes
    path('',redirect_to_register,name='root-redirect')
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
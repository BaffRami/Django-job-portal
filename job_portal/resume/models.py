from django.db import models
from users.models import User
from django.core.validators import FileExtensionValidator

class Resume(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    surname = models.CharField(max_length=100, null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    cv = models.FileField(
        upload_to='resumes/', 
        validators=[FileExtensionValidator(allowed_extensions=['pdf'])],
        verbose_name="Upload Resume (PDF)",
        blank=True,
        null=True,
    )

    def __str__(self):
        return f'{self.first_name} {self.sur_name}'

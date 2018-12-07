from django.db import models
from datetime import date
from django.utils import timezone
from django.contrib.auth.models import User
import uuid

# Create your models here.

class Company(models.Model):
    """Model representing a company."""
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this particular job")
    name = models.CharField(max_length=200, null=True)
    description = models.TextField(max_length = 1000, help_text="Enter a brief description of the company.", null=True, blank=True)	
    emp_number = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name

class JobOffer(models.Model):
    """Model representing a job offer"""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this particular job")
    name = models.CharField(max_length = 200)
    location = models.CharField(max_length = 200)
    deadline = models.DateField(blank=True)	
    salary = models.IntegerField(null=True, blank=True)
    duration = models.IntegerField(null=True, blank=True)
    description = models.TextField(max_length = 1000, help_text="Enter a brief description of the job offer.")
    date_posted = models.DateField(default=timezone.now())	
    recruiter = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    company_id = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, blank=True)
    apply_link = models.URLField(blank=True)
    @property
    def is_over(self):
        if self.deadline < timezone.now():
            return True
        return False

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    job = models.ForeignKey(JobOffer, on_delete=models.SET_NULL, null=True)

class Tag(models.Model):
    job = models.ForeignKey(JobOffer, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length = 40)

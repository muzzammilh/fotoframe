from django.db import models

# creating base models for common fields created_at and updated_at to keep record of date and time
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        

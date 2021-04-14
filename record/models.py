from django.db import models

# Create your models here.
class Record(models.Model):
  record_number = models.CharField(max_length=50, default='python')
  title = models.CharField(max_length=50, default='python')
  expertise_status = models.CharField(max_length=50, default='python')
  payment_status = models.CharField(max_length=50, default='python')
  arrangement_type = models.CharField(max_length=50, default='python')
  updated_state = models.CharField(max_length=50, default='python')
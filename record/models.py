from django.db import models

# Create your models here.
class Record(models.Model):
  record_number = models.CharField(max_length=50, default='python')
  title = models.CharField(max_length=50, default='python')
  expertise_status = models.CharField(max_length=50, default='python')
  payment_status = models.CharField(max_length=50, default='python')
  arrangement_type = models.CharField(max_length=50, default='python')
  action_lawyer = models.CharField(max_length=50, default='python') 
  comments = models.CharField(max_length=550, default='python') 
  dependency = models.CharField(max_length=50, default='python') 
  city = models.CharField(max_length=50, default='python') 
from django.db import models
import datetime

# Create your models here.
class users_data(models.Model):
    email = models.EmailField(primary_key = True)
    firstname = models.CharField(max_length = 50)
    lastname = models.CharField(max_length = 50)
    password = models.CharField(max_length = 255)
    
    class Meta:
        db_table = 'users_data'

class classrooms(models.Model):
    now = datetime.datetime.now()
    email_creator = models.EmailField()
    classroom_id = models.CharField(max_length = 255,primary_key = True)
    classroom_name = models.CharField(max_length = 50)
    class Meta:
        db_table = 'classrooms'

"""
class requests(models.Model):
    is_invitation = models.BooleanField()
    send_by = email = models.EmailField()
    send_to = email = models.EmailField()
    classroom_id = models.CharField(max_length = 255)
    class Meta:
        db_table = 'requests'"""

"""   
class enrollments(models.Model):
    email_creator = models.EmailField(primary_key = True)
    classroom_id = email_creator + now.strftime("%Y-%m-%d-%H-%M-%S-%p")
    classroom_name = models.CharField(max_length = 50)
    class Meta:
        db_table = 'enrollments'"""
        
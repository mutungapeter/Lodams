from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from twilio.rest import Client
from django.core.mail import send_mail, EmailMessage
from . tasks import send_staff_email_notification_task, send_student_email_notification_task
from accounts.models import User
from django.conf import settings




class Intake(models.Model):
    start_year =models.DateField()
    end_year=models.DateField()
    
    def __str__(self):
        return str(self.start_year) +"" "/" +str(self.end_year)



class Course(models.Model):
    course_code = models.CharField(max_length=200, null=True)
    name=models.CharField(max_length=255)
    
    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.CharField(max_length=200)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
class Staff(models.Model):
    employee_number = models.CharField(max_length=200, unique=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    phone_number =models.CharField(max_length=200)
    email = models.EmailField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.name
"""
@receiver(post_save, sender=Staff)
def send_staff_email_notification(sender, instance=None, created=False, **kwargs):
    if instance.name:
        email = instance.user.email
        name = instance.user.staff.name
       
        
        send_staff_email_notification_task.delay(email, name)   
"""
    
  
class Student(models.Model):
    adm_number =  models.CharField(max_length=200, null=True, unique=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    phone_number =models.CharField(max_length=200)
    email = models.EmailField()
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
        
    
    def __str__(self):
        return self.name

"""
@receiver(post_save, sender=Student)
def send_student_email_notification(sender, instance=None, created=False, **kwargs):
    if instance.name:
        email = instance.user.email
        name = instance.user.student.name
       
        
        send_student_email_notification_task.delay(email, name)   
"""
    


  
        
    


class Result(models.Model):
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    subject=models.ForeignKey(Subject,on_delete=models.CASCADE)
    cat_marks=models.FloatField(default=0)
    exam_marks=models.FloatField(default=0)
    total = models.FloatField(default=0, editable=False)    
        
    def __str__(self):
        return self.student.name
    
    def save(self, *args, **kwargs):
        self.total=self.cat_marks+self.exam_marks
        super(Result, self).save(*args, **kwargs)
        
    def  status(self):
        status = ""
        if self.total >= 0 and self.total <= 39:
            status = "Failed"
            
        else:
            status = "Passed"
        return status
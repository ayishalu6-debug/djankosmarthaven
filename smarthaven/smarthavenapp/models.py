from django.db import models

# Create your models here.
class logintable(models.Model):
    username=models.CharField(max_length=30,null=True, blank=True)
    password=models.CharField(max_length=30,null=True, blank=True)
    usertype=models.CharField(max_length=30,null=True, blank=True)
class usertable(models.Model):
    user_id=models.IntegerField(null=True, blank=True)
    LOGIN_ID=models.ForeignKey(logintable, on_delete=models.CASCADE, null=True, blank=True)    
    name=models.CharField(max_length=30,null=True, blank=True)
    address=models.CharField(max_length=30,null=True, blank=True)
    phone=models.IntegerField(null=True, blank=True)
    email=models.CharField(max_length=30,null=True, blank=True)
    
class alerttable(models.Model):
    fieldname=models.CharField(max_length=30,null=True, blank=True)
    alert_id=models.CharField(max_length=30,null=True, blank=True)
    LOGIN_ID=models.ForeignKey(logintable, on_delete=models.CASCADE, null=True, blank=True)
    alert_type=models.CharField(max_length=30,null=True, blank=True)
    alert_message=models.CharField(max_length=30,null=True, blank=True)
    alert_date=models.DateField(null=True, blank=True)
    alert_time=models.IntegerField(null=True, blank=True)
    status=models.CharField(max_length=30,null=True, blank=True)
    
class friendtable(models.Model):
    field_id=models.CharField(max_length=30,null=True, blank=True)
    USER_ID=models.ForeignKey(usertable, on_delete=models.CASCADE,null=True, blank=True)
    friend_user_id=models.IntegerField(null=True, blank=True)
    date=models.DateField(null=True, blank=True)
    status=models.CharField(max_length=30,null=True, blank=True)
class remaindertable(models.Model):
    remainder_id=models.IntegerField(null=True, blank=True)
    user_id=models.IntegerField(null=True, blank=True)
    title=models.CharField(max_length=30,null=True, blank=True)
    description=models.CharField(max_length=30,null=True, blank=True)
    remainder_date=models.DateField(null=True, blank=True)
    remainder_time=models.IntegerField(null=True, blank=True)
    status=models.CharField(max_length=30,null=True, blank=True)
class managementtable(models.Model):
    management_id=models.IntegerField(null=True, blank=True)
    LOGIN_ID=models.ForeignKey(logintable,on_delete=models.CASCADE,null=True, blank=True)
    emergency_number=models.IntegerField(null=True, blank=True)
    description_id=models.CharField(max_length=30,null=True, blank=True)
    created_date=models.DateField(null=True, blank=True)
    status=models.CharField(max_length=30,null=True, blank=True)
class controltable(models.Model):
    control_id=models.IntegerField(null=True, blank=True)
    user_id=models.IntegerField(null=True, blank=True)
    device_name=models.CharField(max_length=30,null=True, blank=True)
    device_type=models.CharField(max_length=30,null=True, blank=True)
    device_status=models.CharField(max_length=30,null=True, blank=True)
    update_date=models.DateField(null=True, blank=True)
class complainttable(models.Model):
    complaint_id=models.IntegerField(null=True, blank=True)
    user_id=models.IntegerField(null=True, blank=True)
    complaint_title=models.CharField(max_length=30,null=True, blank=True)
    complaint_description=models.CharField(max_length=30,null=True, blank=True)
    complaint_date=models.DateField(null=True, blank=True)
    reply=models.CharField(max_length=30,null=True, blank=True)
    reply_date=models.DateField(null=True, blank=True)
    status=models.CharField(max_length=30,null=True, blank=True)

from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.
class Company(models.Model):
    C_ID=models.AutoField(primary_key=True)
    C_logo=models.ImageField(upload_to='images')
    C_Name=models.CharField(max_length=200 ,default="")
    C_Website=models.URLField(max_length=200)
    
class Project1(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()




class template_tracking(models.Model):
    T_id=models.AutoField(primary_key=True)
    C_id=models.ForeignKey(Company, on_delete=models.CASCADE) # secondary key
    template_path=models.CharField(max_length=100 ,default="")
    template_name=models.CharField(max_length=200 ,default="")





class Project(models.Model):
    Project_id=models.AutoField(primary_key=True)
    Project_Name=models.CharField(max_length=100 ,default="")
    company_email=models.EmailField(max_length = 80)
    company_contact_no=models.CharField(max_length=12 ,default="")
    user_id=models.ForeignKey(User, on_delete=models.CASCADE) # secondary key
    C_id=models.ForeignKey(Company, on_delete=models.CASCADE) # secondary key
    Project_type=models.CharField(max_length=100 ,default="") # Modify after conformation # pending good to have addiitional features.
    Project_Desc_or_Scope=models.CharField(max_length=500 ,default="")
    Start_date=models.DateTimeField(default=datetime.date, null=True, blank=True)
    End_date=models.DateTimeField(default=datetime.date, null=True, blank=True)
    
    
class Assessment(models.Model):
    Assesment_id=models.AutoField(primary_key=True)
    Created_by_user_id=models.ForeignKey(User, on_delete=models.CASCADE) # secondary key
    Project_id=models.ForeignKey(Project, on_delete=models.CASCADE) # secondary key
    S_Date=models.DateTimeField(default=datetime.date, null=True, blank=True)
    E_Date=models.DateTimeField(default=datetime.date, null=True, blank=True)
    #Score_Type=models.CharField(max_length=100) # Modify after conformation
    Desc=models.CharField(max_length=500 ,default="")
    Assessment_Type=models.CharField(max_length=100 ,default="") 
    #C_ID=models.ForeignKey(Company, on_delete=models.CASCADE) # secondary key
    Tittle=models.CharField(max_length=200 ,default="")

class Finding(models.Model):
    Finding_id=models.AutoField(primary_key=True)
    Finding_Title=models.CharField(max_length=100,default="")
    Owasp_cat=models.CharField(max_length=100,default="") 
    Desc=models.CharField(max_length=300,default="")
    Technical_impact=models.CharField(max_length=500,default="") 
    Business_impact=models.CharField(max_length=500,default="") 
    CVSS_score=models.FloatField() #float
    CVSS_vector=models.CharField(max_length=100,default="")                                         
    Severity=models.CharField(max_length=100,default="")
    Afftected_resource=models.CharField(max_length=100,default="") 
    Affected_parameter=models.CharField(max_length=100,default="") 
    Remediation=models.CharField(max_length=100,default="") 
    user_id=models.ForeignKey(User, on_delete=models.CASCADE) # secondary key
    Project_id=models.ForeignKey(Project, on_delete=models.CASCADE) # secondary key
    C_id=models.ForeignKey(Company, on_delete=models.CASCADE) # secondary key
    A_id=models.ForeignKey(Assessment, on_delete=models.CASCADE) # secondary key

    
class Assessment_Users(models.Model):
    Assesment_id=models.ForeignKey(Assessment, on_delete=models.CASCADE) # secondary key
    User_id=models.ForeignKey(User, on_delete=models.CASCADE) # secondary key

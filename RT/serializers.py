# this file using for convert complex data type like model instance , qeryset etc into python data type. this process is called Serializer.
# each row in table treated such as object of model. so that each row of table is complex data type.
# This seralize use for creating APIs for backend communication with front end.
# for all above process Django rest frameowork help.
from rest_framework import serializers # immport seralizer of DJango rest frameowork.
from .models import Project,Company,template_tracking,Project,Assessment,Finding ,Assessment_Users # import models

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        fields=( # here mention only those Fields of DB table which you want or like to pass frontend.
            'C_logo',
            'C_Name',
            'C_Website',
            
        )
        model=Company # mention which model you want to Serialize.

# Project Serlaize
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        fields=( # here mention only those Fields of DB table which you want or like to pass frontend.
        
            'Project_Name',
            'company_email',
            'company_contact_no',
            'user_id',
            'C_id',
            'Project_type',
            'Project_Desc_or_Scope',
            'Start_date',
            'End_date',
            
        )
        model=Project # mention which model you want to Serialize.


# Assessment Serlaize
class AssessmentSerializer(serializers.ModelSerializer):
    class Meta:
        fields=( # here mention only those Fields of DB table which you want or like to pass frontend.
        
            'Created_by_user_id',
            'Project_id',
            'S_Date',
            'E_Date',
            'Desc',
            'Assessment_Type',
            'Tittle',
            
        )
        model=Assessment # mention which model you want to Serialize.

 #Assessment Serlaize
class FindingSerializer(serializers.ModelSerializer):
    class Meta:
        fields=( # here mention only those Fields of DB table which you want or like to pass frontend.
        
            'Finding_Title',
            'Owasp_cat',
            'Desc',
            'Technical_impact',
            'Business_impact',
            'CVSS_score',
            'CVSS_vector',
            'Severity',
            'Afftected_resource',
            'Affected_parameter',
            'Remediation',
            'user_id',
            'Project_id',
            'C_id',
            'A_id',
            
        )
        model=Finding # mention which model you want to Serialize.
 
 # Assessment_Users
class Assessment_UsersSerializer(serializers.ModelSerializer):
    class Meta:
        fields=( # here mention only those Fields of DB table which you want or like to pass frontend.
            'Assesment_id',
            'User_id',

            
        )
        model=Assessment_Users # mention which model you want to Serialize.

 # template tracking
class template_trackingSerializer(serializers.ModelSerializer):
    class Meta:
        fields=( # here mention only those Fields of DB table which you want or like to pass frontend.
            'C_id',
            'template_path',
            'template_name',

            
        )
        model=template_tracking # mention which model you want to Serialize.

from .models import Project,Company,template_tracking,Assessment,Finding,Assessment_Users
from .serializers import ProjectSerializer
from .serializers import CompanySerializer
from .serializers import AssessmentSerializer
from .serializers import FindingSerializer
from .serializers import Assessment_UsersSerializer
from .serializers import template_trackingSerializer

from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer # for json render
from django.shortcuts import render
# Create your views here.
def CompanyList(request): # API of company table. or data.
    C_queryset=Company.objects.all() # get all instance of model or queryset.

    C_serializer=CompanySerializer(C_queryset,many=True) # convert complex query into python data structure that is called seralizers
    C_json_data=JSONRenderer().render(C_serializer.data) # convert python data structure into json format or structure for send json data to fronend or to any applications.
    return HttpResponse(C_json_data,content_type='application/json') # render json data to frontend. 
def ProjectList(request):
    P_queryset=Project.objects.all()

    P_serializer=ProjectSerializer(P_queryset,many=True)
    P_json_data=JSONRenderer().render(P_serializer.data)
    return HttpResponse(P_json_data,content_type='application/json')
def AssessmentList(request):
    A_queryset=Assessment.objects.all()

    A_serializer=AssessmentSerializer(A_queryset,many=True)
    A_json_data=JSONRenderer().render(A_serializer.data)
    return HttpResponse(A_json_data,content_type='application/json')
def FindingList(request):
    F_queryset=Finding.objects.all()

    F_serializer=FindingSerializer(F_queryset,many=True)
    F_json_data=JSONRenderer().render(F_serializer.data)
    return HttpResponse(F_json_data,content_type='application/json')
def Assessment_UserList(request):
    AU_queryset=Assessment_Users.objects.all()

    AU_serializer=Assessment_UsersSerializer(AU_queryset,many=True)
    AU_json_data=JSONRenderer().render(AU_serializer.data)
    return HttpResponse(AU_json_data,content_type='application/json')

def template_trackingList(request):
    tt_queryset=template_tracking.objects.all()

    tt_serializer=template_trackingSerializer(tt_queryset,many=True)
    tt_json_data=JSONRenderer().render(tt_serializer.data)
    return HttpResponse(tt_json_data,content_type='application/json')


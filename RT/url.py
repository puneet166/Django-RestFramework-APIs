from django.urls import path
from RT import views
from django.contrib import admin
from django.contrib.auth import views as auth_views 
urlpatterns=[
    path('company',views.CompanyList),

    path('project',views.ProjectList),
    path('template_tracking',views.template_trackingList),
    path('Assessment',views.AssessmentList),
    path('Finding',views.FindingList),
    path('Assessment_Users',views.Assessment_UserList),
    

]
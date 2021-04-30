from django.contrib import admin
from RT.models import Project,Company,Assessment,Finding,Project1

# Register your models here for admin
admin.site.register(Project)
admin.site.register(Company)
admin.site.register(Assessment)
admin.site.register(Finding)

admin.site.register(Project1)

from django.contrib import admin
from .models import MainSection, Sector, Stat, Service, Project, Team, BucoInfo
# Register your models here.

admin.site.register(MainSection)

admin.site.register(Sector)

admin.site.register(Stat)

admin.site.register(Team)

admin.site.register(BucoInfo)

admin.site.register(Project)



class ProjectInline(admin.StackedInline):
    model = Project
    extra = 1
   
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    inlines = [
        ProjectInline,
    ]

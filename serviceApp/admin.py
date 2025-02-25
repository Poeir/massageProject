from django.contrib import admin

# Register your models here.
from .models import Service


class serviceAdmin(admin.ModelAdmin):
    list_display = ['ServiceID','Name','Price','Duration']
    search_fields = ['Name',]

admin.site.register(Service,serviceAdmin)
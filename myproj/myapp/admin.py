import imp
from django.contrib import admin
from .models import *
# Register your models here.
admin.site.site_header="My login page"
# admin.site.register(Student)


# from django.contrib import admin
# from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=('firstname','lastname')
    list_filter= ("per","city")
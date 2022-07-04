from django.contrib import admin
from .models import *

# Register your models here.

admin.site.site_title = "Lodams College Portal"
admin.site.site_header = "Lodams College Portal"
admin.site.index_title = "Results Portal"
admin.site.register(Course)   
admin.site.register(Intake)
admin.site.register(Subject)
admin.site.register(Student)
admin.site.register(Result)
admin.site.register(Staff)



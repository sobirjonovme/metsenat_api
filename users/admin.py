from django.contrib import admin

from .models import Sponsor, University, Student


# Register your models here.
admin.site.register(Sponsor)
admin.site.register(University)
admin.site.register(Student)

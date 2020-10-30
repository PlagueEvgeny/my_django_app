from django.contrib import admin

from mainapp.models import SubjectCategory
from mainapp.models import Course

admin.site.register(SubjectCategory)
admin.site.register(Course)
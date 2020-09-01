from django.contrib import admin
# Register your models here.

from mywebsite.models import exam
from mywebsite.models import paper
from mywebsite.models import login

admin.site.register(exam)
admin.site.register(paper)
admin.site.register(login)  



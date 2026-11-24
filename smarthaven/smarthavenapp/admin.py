from django.contrib import admin

from .models import alerttable, complainttable, controltable, friendtable, logintable, managementtable, remaindertable, usertable

# Register your models here.
admin.site.register(logintable)
admin.site.register(usertable)
admin.site.register(alerttable)
admin.site.register(friendtable)
admin.site.register(remaindertable)
admin.site.register(managementtable)
admin.site.register(controltable)
admin.site.register(complainttable)
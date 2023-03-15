from django.contrib import admin
from .models import Customer,Contact,Team

class CustomerAdmin(admin.ModelAdmin):
           list_display=('pk','name','email','phone','location',)
admin.site.register(Customer,CustomerAdmin)

class ContactAdmin(admin.ModelAdmin):
           list_display=('pk','name','email','desc',)
admin.site.register(Contact,ContactAdmin)

class TeamAdmin(admin.ModelAdmin):
           list_display=('pk','name','email','role',)
admin.site.register(Team,TeamAdmin)
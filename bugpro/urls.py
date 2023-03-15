
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('bugapp.urls')),
]


admin.site.index_title ="The Issue Tracker"
admin.site.site_header ="The Issue Tracker Admin"
admin.site.site_title ="Issue Management"
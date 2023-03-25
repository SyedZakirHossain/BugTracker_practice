from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('bugapp.urls')),
]
if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)   

admin.site.index_title ="The Issue Tracker"
admin.site.site_header ="The Issue Tracker Admin"
admin.site.site_title ="Issue Management"

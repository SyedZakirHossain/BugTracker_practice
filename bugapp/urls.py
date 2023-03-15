from django.urls import path
from.import views
from django.contrib import admin
from django.contrib.auth import views as auth_views


app_name = "bugapp"


urlpatterns = [
            path('',views.home,name='home'),    # domain name will be pest here.
            path('admin', views.admin, name="admin"),
            path('contact/', views.contact, name="contact"),
            path('contact/contactsave', views.contactsave, name="contactsave"),
            path('enter2/', views.enter2, name="enter2"),
            path('login/', views.login, name="login"),
            
            path('xx', views.asigned_to, name="asigned_to"),
            path('issue_detail', views.issue_detail, name="issue_detail"),
            path('login/enter2', views.enter2, name="enter2"),
            path('login_page/', views.login_page, name="login_page"),
            path('logout/', auth_views.LogoutView.as_view(template_name='logout.html',
                next_page=None), name="logout"),
            
            #path('notice/', views.notice, name='notice'),
            #path('noticepublish/noticesave', views.noticesave, name='noticesave'),
            path('all_issue/', views.all_issue, name='all_issue'),
            
            path('register/', views.register, name="register"),
            path('register2/register', views.register, name="register2"),
            path('register2/', views.register2, name="register2"),
            path('search/', views.search, name="search"),
            path('userhome/', views.userhome, name="userhome"),
           ]

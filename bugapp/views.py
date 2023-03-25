from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import Group, User
from django.http import HttpResponse
from .models import Team


import io
import json
import os
import random


from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.http import (FileResponse, HttpResponse, HttpResponseRedirect,
                         JsonResponse)

from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from .decorators import unauthenticated_user,allowed_users,admin_only
from bugapp import forms
from .models import Contact,Customer


@allowed_users(allowed_roles=['admin'])
def admin(request):
    return render(request, 'admin.site.urls')

#========================================================= 
@login_required(login_url="/login")
def contact(request):
    return render(request, "contact.html")
#========================================================= 

def contactsave(request):
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/all_issue')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})
#========================================================= 


@unauthenticated_user
#@allowed_users(allowed_roles=['admin'])
def enter2(request):
    cap = request.POST.get("captha")
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if str(cap) != str_num:
            return HttpResponse("<h4>Error captha</h4>")
        if user is not None:
            auth.login(request, user)
            return redirect('/userhome')
        else:
            messages.info(request, 'Invalid credentials')
            # return render(request,'login.html')
            return redirect('/login')
    else:
        messages.info(request, 'Invalid credentials')
        return render(request, '/login')


#=========================================================

def home(request):
    data = {
       
        'title': 'Home Page, Welcome To bug tracker page.',
        'bdata': 'I am a full stack developer.',
        
    }
    return render(request, 'home.html', context=data)


# =========================================================
def login_page(request):
    return render(request, 'logout.html')
#========================================================= 

def login(request):
    num = random.randrange(11212, 98998)
    global str_num
    str_num = str(num)
    return render(request, "login.html", {"img": str_num})

# ===========================================

#@allowed_users(allowed_roles=['admin'])
@login_required(login_url='/login')
def all_issue(request):
    #queryset = Notice.objects.all().order_by('-pk')
    n = Contact.objects.all().order_by('-pk')
    data = {
        'contact': n,
        
    }
    return render(request, 'issue_view.html', context=data)

#========================================================= 



def register(request):
    r = Contact.objects.all()
    u = User.objects.all()
    dict = {'student': r, 'skul': 'Barishal Zilla School',
            'x': u}
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username taken')
                return redirect('/register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email taken')
                return redirect('/register')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email)
                user.save()

                group = Group.objects.get(name='student')
                user.groups.add(group)
                messages.info(request, 'Account created for :-  ' + username)
                return redirect('/login')
        else:
            messages.info(request, 'Password not matching')
            return redirect('/register')
    else:
        return render(request, 'register.html', context=dict)
    
# =========================================================

def register2(request):
            
    return render(request,'register.html')   
#=========================================================

@login_required(login_url='/login')
#@allowed_users(allowed_roles=['admin'])
#@admin_only
def userhome(request):
    r = Contact.objects.all()
    u = User.objects.all()
    dict = {'student': r, 
             'x': u}

    return render(request, 'userhome.html', context=dict)
#=========================================================
def asigned_to(request):
    issue = Contact.objects.filter(user=1)
     #issue = Contact.objects.all()
    #team = Team.objects.all()
    #team = Team.objects.get(pk=1)
    dict = {'issue': issue,
             }

    return render(request, 'asigned_to.html', context=dict)
#=========================================================
def issue_detail(request,issue_id):
    i = Contact.objects.get(pk=issue_id)
    context = {
        'issue': i,
        
    }
    return render(request, 'issue_detail.html', context=context)

#========================================================= 
#def search(request):
    #return render(request, 'search.html')
def search(request):
    # get the search query from the request
    query = request.GET.get('q')

    # get the preset values from a database or other data source
    preset_values = ['Option 1', 'Option 2', 'Option 3']

    context = {
        'query': query,
        'preset_values': preset_values
    }
    return render(request, 'search.html', context)

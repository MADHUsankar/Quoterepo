# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User 
from django.core.urlresolvers import reverse

# Create your views here.
def index(request):
    #User.objects.all().delete()
 
    return render(request,'app_reglogin/index.html' )

def registration(request):
    result = User.objects.register(request.POST)
    if not result['status']:
        for error in result['errors']:
            messages.error(request,error)
        return redirect(reverse('users:my_index'))
    else:
        messages.success(request,"Successful")
        request.session['userid'] = result['user'].id   
        request.session['name'] = result['user'].name
        return redirect(reverse('quotes:homepage'))
 
def loginuser(request):
    result = User.objects.loginval(request.POST)
    
    if not result['status']:
        for error in result['errors']:
            messages.error(request,error)
        return redirect(reverse('users:my_index'))
    else:
        messages.success(request,"Successful")
        request.session['userid'] = result['user'].id
        request.session['name'] = result['user'].name
        return redirect(reverse('quotes:homepage'))

def logout(request):
    request.session.flush()
    return redirect('/')


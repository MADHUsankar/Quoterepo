# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages
from ..app_reglogin.models import User
from .models import Quote
from django.core.urlresolvers import reverse

# Create your views here.
def homepage(request):
    if not 'userid' in request.session:
        return redirect(reverse('users:my_index'))
    #Tripschedule.objects.all().delete()
    currentuser = User.objects.get(id=request.session['userid'])
    context = {
                      
                    #"quotes" : Quote.objects.all(),
                    # 'user1': User.objects.get(id=request.session['userid']),
                    'Userfavs' :  Quote.objects.all().filter(favquotes=currentuser),
                    'Otheruserfavs' :  Quote.objects.all().exclude(favquotes=currentuser) ,
                    "name": request.session['name'],             
                    "userid" :  request.session['userid'] 
                }
   
    return render(request,'app_quote/homepage.html', context)


def addquote(request):
    if not 'userid' in request.session:
        return redirect(reverse('users:my_index'))

    if request.method == "POST":
        print request.POST
        context = {
                "name": request.session['name'],
                "userid" :  request.session['userid'] 
                }
      
        result = Quote.objects.addquote(request.POST,context)
        print  result['status']
        if not result['status']:
             
            for error in result['errors']:
                messages.error(request,error)
                print "here"
            return redirect(reverse('quotes:homepage'))
        else: 
            messages.success(request,"Successful")
            return redirect(reverse('quotes:homepage'))
            
    else:
            print "ENTERED GET"
            context = {
                    #"quotes" : Quote.objects.all(),
                    # 'user1': User.objects.get(id=request.session['userid']),
                    'Userfavs' :  Quote.objects.all().filter(favquotes=currentuser),
                    'Otheruserfavs' :  Quote.objects.all().exclude(favquotes=currentuser) ,
                    "name": request.session['name'],             
                    "userid" :  request.session['userid'] 
             }
    return render(request,'app_quote/homepage.html',context )

def addfavquote(request,id):    
    if not 'userid' in request.session:
        return redirect(reverse('users:my_index'))
    context = {
                "quoteid" :id,
                "userid" :  request.session['userid'] ,
                "name": request.session['name']
                }
    result = Quote.objects.addfavquote(context)
    if not result['status']:
            for error in result['errors']:
                messages.error(request,error)
                print "here"
            #return redirect(reverse('secrets:add_like',kwargs={'id': id}))
            return redirect(reverse('quotes:homepage'))
    else: 
            messages.success(request,"Successful")
            return redirect(reverse('quotes:homepage'))

def  removefavquote(request,id):
    if not 'userid' in request.session:
        return redirect(reverse('users:my_index'))
    context = {
                "quoteid" :id,
                "userid" :  request.session['userid'] ,
                "name": request.session['name']
                }
    result = Quote.objects.removefavquote(context)

    if not result['status']:
            for error in result['errors']:
                messages.error(request,error)
                print "here"
            #return redirect(reverse('secrets:add_like',kwargs={'id': id}))
            return redirect(reverse('quotes:homepage'))
    else: 
            messages.success(request,"Successful")
            return redirect(reverse('quotes:homepage'))

def showuser(request,id):
    if not 'userid' in request.session:
        return redirect(reverse('users:my_index'))
    context = {
        'userdata' :User.objects.get(id=id),
        'quoteuser' :Quote.objects.filter((quotecreator__id)=id).distinct(),
        'quotecount':Quote.objects.filter((quotecreator__id)=id).count(),
        'quotes':Quote.objects.filter((quotecreator__id)=id),
        }
        #return redirect(reverse('show',kwargs={'id':id}))
    return render(request,'app_quote/showuser.html', context)

def  delquote(request,id):
    if not 'userid' in request.session:
        return redirect(reverse('users:my_index'))

    Quote.objects.filter(id=id).delete()
    return redirect(reverse('quotes:homepage'))


def editquote(request,id):
    if not 'userid' in request.session:
        return redirect(reverse('users:my_index'))

    if request.method == "POST":
        context = {
                "name": request.session['name'],
                "userid" :request.session['userid'],
                "quoteid" : id
                }
        
        result = Quote.objects.editquote(request.POST,context)
        print  result['status']
        if not result['status']:
             
            for error in result['errors']:
                messages.error(request,error)
                print "here"
                return redirect(reverse('quotes:editquote',kwargs={'id': id}))
        else: 
            messages.success(request,"Successful")
            return redirect(reverse('quotes:homepage'))
    else:
        context = {
            'quote' :Quote.objects.get(id=id)

            }
            #return redirect(reverse('show',kwargs={'id':id}))
    return render(request,'app_quote/editquote.html', context)
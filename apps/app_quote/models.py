# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ..app_reglogin.models import User
from django.db import models
from datetime import date
from datetime import datetime
import time 
import bcrypt
 
class quoteManager(models.Manager):
    def addquote(request,postData,sessiondata):
        print postData
        print " In addquote %%%%%%%%%%%"
        
        results = {'status': True, 'errors': []}
        if not postData['quotedby'] or len(postData['quotedby'])<1:
            print "In quotedby "
            results['status'] = False
            results['errors'].append("Please enter a Quoted By")

        elif not postData['quotedby'] or len(postData['quotedby'])<3:
            print "In quotedby "
            results['status'] = False
            results['errors'].append("Quoted By should be atleast three characters")

        if not postData['message'] or len(postData['message'])<1:
            print "In message "
            results['status'] = False
            results['errors'].append("Please enter a Message")

        elif not postData['message'] or len(postData['message'])<10:
            print "In message "
            results['status'] = False
            results['errors'].append("Message should be atleast 10 characters")

 
 
 
        if results['status']:
            user1 = User.objects.get(id = sessiondata['userid'])
            Quote1 = Quote.objects.create(quotetext=postData['message'],
            quotedby=postData['quotedby'],quotecreator = user1)    
            results['status'] = True
            print "Successfully done!!!!!!!!!"
       
        return results   

    def addfavquote(request,context):
        print context
        results = {'status': True, 'errors': []}

        quote1=Quote.objects.get(id=context["quoteid"])
        user1=User.objects.get(id=context["userid"])
        quote1.favquotes.add(user1) 
        results['status'] = True
        return results 

    def removefavquote(request,context):
        print context
        results = {'status': True, 'errors': []}

        quote1=Quote.objects.get(id=context["quoteid"])
        user1=User.objects.get(id=context["userid"])
        quote1.favquotes.remove(user1) 
        results['status'] = True
        return results 

    def editquote(request,postData,sessiondata):
        print postData
        print " In editappt %%%%%%%%%%%"
        
        results = {'status': True, 'errors': []}
        if not postData['quotedby'] or len(postData['quotedby'])<1:
            print "In tasks "
            results['status'] = False
            results['errors'].append("Please enter a Quoted by")

 
        if not postData['message'] or len(postData['message'])<1:
            print "In startdate "
            results['status'] = False
            results['errors'].append("Please enter a message ")

        if results['status']:
            user1 = User.objects.get(id = sessiondata['userid'])
            quote1 = Quote.objects.get(id=sessiondata['quoteid'])
            quote1.quotetext = postData['message'] 
            quote1.quotedby=postData['quotedby']
             
            quote1.save()
             
        return results            


class Quote(models.Model):
    quotetext = models.TextField(max_length=1000)
    quotedby = models.CharField(max_length=150)
    quotecreator = models.ForeignKey('app_reglogin.User', related_name="quotecreators")
    favquotes = models.ManyToManyField('app_reglogin.User', related_name="favquotes")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
     
    objects=quoteManager()
    #bookauthors
    #bookreviews
 
    


from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from random import randint
import urllib2
import urllib
import json

from .models import Contact, Messeges

def contact_create(request):
	if request.method == 'POST':
		#print request.POST
		contactName = request.POST.get('name')
		contactNumber = request.POST.get('number')
		#print contactName
		#print contactNumber
		Contact.objects.create(
				name = contactName,
				number = contactNumber
		)
		
		return HttpResponse('success')

def contact_list(request):
	contact_data = Contact.objects.all().order_by("-dateadded")
	context = {
		"title" : "Contacts Home",
		"data" : contact_data
	}
	return render(request, "contact_list.html", context)
	pass

def contact_details(request, id=None):
	instance = get_object_or_404(Contact, id=id)
	#generate random otp
	#if post from view call sms api
	otp = randint(100000,999999)

	context = {
		"title" : instance.name,
		"instance" : instance,
		"otp" : otp
	}

	if request.method == 'POST':
		message = request.POST.get('otp')
		#print message
		user = str('myfoodzilla')
		password = str('9953833404')
		sender = str('pranay')
		number = instance.number

		url = 'http://login.bulksmsgateway.in/sendmessage.php?'+urllib.urlencode({'user': user, 'password': password, 'mobile': number, 'message': message, 'sender': sender, 'type': '3'})
		req = urllib2.Request(url)	

		try:
			page = urllib2.urlopen(req)
		except urllib2.HTTPError, e:
			print e.fp.read()
		content = page.read()
		data = json.loads(content)
		status = data.get('status')
		if status == 'success':
			print 'success'
			Messeges.objects.create(
				name=instance.name,
				number=number,
				message=message
				)
			message_data = Messeges.objects.all().order_by("-senton")
			context = {
					"title" : "Sent Messages",
					"data" : message_data
					}
			return render(request, "sent_messages.html", context)
			pass
				
	return render(request, "contact_detail.html", context)
	

def sent_sms(request):
	message_data = Messeges.objects.all().order_by("-senton")
	context = {
		"title" : "Sent Messages",
		"data" : message_data
	}
	return render(request, "sent_messages.html", context)
	pass
from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.


class Contact(models.Model):
	"""docstring for ClassName"""
	name = models.CharField(max_length=120)
	number = models.CharField(max_length=12)
	dateadded = models.DateTimeField(auto_now=False, auto_now_add=True)

	def __unicode__(self):
		return self.name

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse("contact:detail", kwargs={"id": self.id})


class Messeges(models.Model):
	"""docstring for SentMesseges"""
	name = models.CharField(max_length=120)
	number = models.CharField(max_length=12)
	message = models.CharField(max_length=180)
	senton = models.DateTimeField(auto_now=False, auto_now_add=True)

	def __unicode__(self):
		return self.name

	def __str__(self):
		return self.name
		
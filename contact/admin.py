from django.contrib import admin

# Register your models here.

from .models import Contact, Messeges


class ContactModelAdmin(admin.ModelAdmin):
	list_display = ["name", "dateadded"]
	search_fields = ["name", "number"]

	class meta:
		model = Contact


class MessegesModelAdmin(admin.ModelAdmin):
	list_display = ["name", "senton"]
	search_fields = ["name", "number"]

	class meta:
		model = Messeges

# this line is to register the posts app to the admin
admin.site.register(Contact, ContactModelAdmin)
admin.site.register(Messeges, MessegesModelAdmin)
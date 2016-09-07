from django.conf.urls import url
from django.contrib import admin

"""
	url routing for the app posts
"""
from  contact.views import(
	contact_create,
	contact_list,
	sent_sms,
	contact_details
)

urlpatterns = [
    url(r'^$', contact_list, name="list"),
    url(r'^create/$', contact_create, name="add"),
    url(r'^sent-messages/$', sent_sms, name="sent"),
    url(r'^(?P<id>\d+)/$', contact_details, name="detail"),
    #url(r'^edit/(?P<id>\d+)/$', post_update, name="edit"),
    #url(r'^(?P<id>\d+)/$', post_detail, name="detail"),
    #url(r'^(?P<id>\d+)/delete/$', post_delete, name="delete"),
    #url(r'^login/$', login, name="login"),

]
# go through vid 19 again for url better routing
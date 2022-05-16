from django.contrib import admin
from connect_app.models import Message
from members.models import Member

admin.site.register(Member)
# admin.site.register(Interest)
admin.site.register(Message)
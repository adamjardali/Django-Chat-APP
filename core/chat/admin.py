from django.contrib import admin

from .models import User,Contact, Chat, Message

admin.site.register(User)
admin.site.register(Chat)
admin.site.register(Contact)
admin.site.register(Message)
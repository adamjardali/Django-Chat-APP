from django.db import models

from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver


class User(AbstractUser):
    """
    Custom User Model
    In case you want to customize the User Model
    Ensure to update the `settings.AUTH_USER_MODEL` value
    """

    picture = models.ImageField(upload_to="profile_pictures/", blank=True, null=True)
    bio = models.CharField(max_length=255, blank=True, null=True)
    jobTitle = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={"username": self.username})

    def get_profile_name(self):
        return self.username


class Contact(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	freinds = models.ManyToManyField('self',blank=True)

	def __str__(self):
		return self.user.username

class Message(models.Model):
    contact = models.ForeignKey(
        Contact, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField(blank=True,default="Hello World!")
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.contact.user.username


class Chat(models.Model):
    participants = models.ManyToManyField(
        Contact, related_name='chats', blank=True)
    messages = models.ManyToManyField(Message, blank=True)

    def __str__(self):
        return "{}".format(self.pk)
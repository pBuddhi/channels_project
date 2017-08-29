from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Room(models.Model):
	"""
	A room for people to chat in.
	"""

	# Room title
	title = models.CharField(max_length=255)

	def __str__(self):
		return self.title

class Message(models.Model):
	
	title = models.CharField(max_length=255)
	user = models.ForeignKey(User,null=True)
	room = models.ForeignKey(Room)

	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title


from django.db import models

# Create your models here.
class Room(models.Model):
    """
    A room for people to chat in.
    """

    # Room title
    title = models.CharField(max_length=255)

    def str(self):
        return self.title
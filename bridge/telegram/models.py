from django.db import models


class Channel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    channel_id = models.IntegerField()
    name = models.TextField()

    def __str__(self):
        return f"Name: {self.name} id: {self.channel_id}"

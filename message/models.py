from django.db import models


class Comment(models.Model):
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment {self.id}'

# Create your models here.
class Message(models.Model):
    content = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
    upvotes = models.IntegerField(default=0)
    comments = models.ManyToManyField(Comment, related_name='message_comments', blank=True,
        null=True)

    def __str__(self):
        return f'Message {self.id}'
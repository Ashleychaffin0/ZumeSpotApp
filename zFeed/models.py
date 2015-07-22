from django.db import models
import datetime

# Create your models here.

class User(models.Model):
    handle = models.CharField(max_length=100)
    initial_followers = models.IntegerField()
    klout_score = models.IntegerField()
    timestamp = models.DateTimeField(default=datetime.datetime.now)
    oauth_token = models.CharField(max_length=100)
    oauth_token_secret = models.CharField(max_length=100)

    def __str__(self):              # __unicode__ on Python 2
        return "%s" % (self.handle)




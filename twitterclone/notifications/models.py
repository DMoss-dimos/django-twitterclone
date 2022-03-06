from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.db.models.deletion import CASCADE
from twitter_user.models import User_Profile
from tweet.models import Post

# Create your models here.

class Notification(models.Model):
    tweetie = models.ForeignKey(User_Profile, on_delete=models.CASCADE)
    tweet = models.ForeignKey(Post, on_delete=models.CASCADE)

from twitter_clone.settings import TIME_ZONE
from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey
from twitter_user.models import User_Profile



# class Follow(models.Model):
#     user_follow = models.ForeignKey(User,related_name='users_follow', on_delete=models.CASCADE)
#     follow_date = models.DateTimeField(auto_now_add=True, blank=True)
#     follower = models.ForeignKey(User,related_name='users_follow', on_delete=models.CASCADE)


#     def __str__(self):
#         return self.username

# class Comments(models.Model):
#     comment_date = models.DateTimeField(auto_noew_add=True)
#     comment_author = models.ForeignKey(User, on_delete=CASCADE)
#     comment_post = models.ForeignKey(User, on_delete=models.CASCADE)
#     tweet = models.TextField(max_length=250)
#     likes = models.IntegerField(default=0)
#     dislikes = models.IntegerField(default=0)


class Post(models.Model):
    post_content = models.TextField(max_length=250)
    post_date = models.DateTimeField(auto_now=True)
    post_author = models.ForeignKey(User_Profile, on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

    def __str__(self):
        return self.post_content[:20]
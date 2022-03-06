
from django.contrib import admin
from django.urls import path, include
from tweet import views



urlpatterns = [
    # path('', views.index, name='home'),
    path("like/<int:post_id>/", views.like_view, name="like"),
    path("dislike/<int:post_id>/", views.dislike_view, name="dislike"),
    path("post/", views.post_view, name="form"),
    path("tweet_detail/<int:tweet_id>/", views.tweet_view, name="tweet_view"),
    path("add/", views.add_tweet, name="add")
]
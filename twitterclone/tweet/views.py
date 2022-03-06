from django.shortcuts import render, HttpResponseRedirect, redirect
from tweet.models import Post
from django.urls import reverse
from tweet.forms import PostForm
import platform
import subprocess as sp
import re
from twitter_user.models import User_Profile
from notifications.models import Notification
from django.contrib.auth.decorators import login_required



# @login_required
def tweet_view(request, tweet_id):
    # post = Post.objects.all()
    # tweets = Post.objects.filter(
    #     author_follow = request.user) | Post.objects.filter(author=request.user).order_by("-post_date"
    # )
    tweet = Post.objects.get(id=tweet_id)
    return render(request, 'tweet_detail.html', {'tweet': tweet})


# def user_tweet(request):
#     x = ""

#     if request.method == "POST":
#         forms = PostForm(request.POST)
#         if forms.is_valid():
#             text_words = forms.cleaned_data["post_content"]
#             Post.objects.create(tweet_text=text_words)
#             if platform.system() == "Windows":
#                 computer_shell = True
#             else:
#                 computer_shell = False
#             x = sp.check_output(
#                 ['usertweet', text_words ], universal_newlines=True, stderr=sp.STDOUT)
#     forms = PostForm()
#     return render(request, "tweet_detail.html", {"forms": forms, "sp": x})

# @login_required()
def add_tweet(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            # form.save()
            data = form.cleaned_data
            tweet = Post.objects.create(
                post_content=data["post_content"],
                post_author=request.user
            )
            if "@" in data["post_content"]:
                find_user = re.findall(r"@(\w+)", data["post_content"])
                grap_user = find_user[0]
                user = User_Profile.objects.get(username=grap_user)
                Notification.objects.create(tweetie=user,tweet=tweet)
            return redirect('/')

    form = PostForm()
    return render(request, "add_user.html", {"form": form})


def like_view(request, post_id):
    post = Post.objects.get(id=post_id)
    post.likes += 1
    post.save()
    return HttpResponseRedirect("/")


def dislike_view(request, post_id):
    post = Post.objects.get(id=post_id)
    post.dislikes += 1
    post.save()
    return HttpResponseRedirect("/")


def post_view(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Post.objects.create(
                post_content=data["post_content"],
                post_author=request.user
                )

            return HttpResponseRedirect(reverse("home"))

    form = PostForm()
    return render(request, 'tweet_detail.html', {"form": form})
    # return HttpResponseRedirect("/")
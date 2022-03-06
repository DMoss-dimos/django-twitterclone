from django import forms
from tweet.models import Post


class PostForm(forms.Form):
    post_content= forms.CharField(max_length=140)
    # class Meta:
    #     model = Post
    #     fields = ["post_content"]
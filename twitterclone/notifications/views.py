from django.shortcuts import render
from django.contrib.auth.models import User
from tweet.models import Post
# from tweet.views import
from .models import Notification
from twitter_user.models import User_Profile


def notification(request, users):
    """
    Arguments

        :name: notification name (string)
        :users: user object or list of user objects
        :context: additional context for notification templates (dict)

    Returns

        None
    """

    user_p = User_Profile.objects.get(id=users)
    notice_p = Notification.objects.filter(tweetie=user_p)
    return render(request, "notifications.html", {"notice_p":notice_p, "user_p":user_p})
    # notification = Notification.objects.get(name=name)
    # return notification.send(users)

#Notes
# not usre this is right
# def notifications(request):
#     if request.user.is_authenticated:
#         return{"notifications":request.user.Notification.filter(is_read=False)}
#     else:
#         return{"notifications": []}
        # Not sure but I think this may go in setting in templates
        # under "context_processors" "apps.notifications.somepythonfolder.nitifications"
        # in html {{notifications.count}}
from django.db import models

from django.contrib.auth.models import User

# ------------------------------ #
# --- --- --- MODELS --- --- --- #
# ------------------------------ #

class Task(models.Model):

    title = models.CharField(max_length=100, null=True)
    content = models.CharField(max_length=1000, null=True, blank=True)
    date_posted = models.DateTimeField(auto_now_add=True, null=True)

    user = models.ForeignKey(User, max_length=10, on_delete=models.CASCADE, null=True)


class Profile(models.Model):

    profile_pic = models.ImageField(null=True, blank=True, upload_to="images/", default='/defaultuser.png')
    user = models.ForeignKey(User, max_length=10, on_delete=models.CASCADE, null=True)
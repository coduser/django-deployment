from django.db import models
from django.contrib.auth.models import User

# username, password, email from builtin django admin

# Create your models here.
# don't name any class with as User because it is a default Table/Model in Django database
class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    facebook_id = models.URLField(blank=True)

    profile_pic = models.ImageField(upload_to="profile_pics", blank=True)

    def __str__(self):
        return self.user.username

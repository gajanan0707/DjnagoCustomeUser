from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _


# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(
        _('email address'), max_length=254, unique=True, null=True, blank=True)
    avtar = models.ImageField(upload_to='thumbpath', blank=True)

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'

class UserProfile(models.Model):  
    User = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.User.first_name + " - " + self.User.last_name
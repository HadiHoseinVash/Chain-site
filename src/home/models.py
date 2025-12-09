from django.db import models
from django.contrib.auth.models import User
from PIL import Image
import datetime
import os

def user_directory_path(instance,filename):
    today = datetime.date.today()
    # مسیر: media/سال/ماه/روز/
    return os.path.join(
        str(today.year),
        str(today.month).zfill(2),
        str(today.day).zfill(2),
        filename
    )

class Photo(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    img = models.ImageField(upload_to=user_directory_path)

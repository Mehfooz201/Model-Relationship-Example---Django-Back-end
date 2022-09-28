from statistics import mode
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Page(models.Model):
    #------------------- One to One Relation -------------------------------------
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, limit_choices_to = {'is_staff':True})

    page_name = models.CharField(max_length=70)
    page_cat = models.CharField(max_length=70)
    page_pub_date = models.DateField()


class Post(models.Model):
    #------------------- Many to One Relation -------------------------------------
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    post_name = models.CharField(max_length=70)
    post_cat = models.CharField(max_length=70)
    post_pub_date = models.DateField()


class Song(models.Model):
    #------------------- Many to Many Relation -------------------------------------
    user = models.ManyToManyField(User)

    song_name = models.CharField(max_length=70)
    song_duration = models.IntegerField()
    song_pub_date = models.DateField()

    def written_by(self): 
        return ",   ".join([str(p) for p in self.user.all()])
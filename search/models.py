from django.db import models


# Create your models here.

class Post(models.Model):
      postname = models.CharField(max_length=50)
      contents = models.TextField()

      def __str__(self):
          return self.postname

class Champion(models.Model):
      number = models.IntegerField()
      name = models.CharField(max_length=255, null = True)
      job = models.CharField(max_length=50, null = True)
      type = models.TextField()
      def __str__(self):
          return self.name

class Video(models.Model):
    title = models.CharField(max_length=200)
    video_key = models.CharField(max_length=12)


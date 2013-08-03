from django.db import models

# Create your models here.

class Album(models.Model):
    year = models.IntegerField()
    event = models.CharField(max_length=255)
    total_pictures = models.IntegerField()
    def __unicode__(self):
        return str(self.year)+": "+str(self.event)


class Picture(models.Model):
    album = models.ForeignKey(Album)
    src = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    def __unicode__(self):
        return self.name

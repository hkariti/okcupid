from django.db import models

# Create your models here.
class User(models.Model):
    url = models.CharField(max_length=1000)

    def __unicode__(self):
        return self.url

class Question(models.Model):
    id = models.IntegerField(primary_key=True)
    text = models.CharField(max_length=10000)
    users = models.ManyToManyField(User)

    def __unicode__(self):
        return self.text

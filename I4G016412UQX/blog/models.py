from django.db import models

# Create your models here.

class Post(models.Model):

    title = models.CharField(max_length=200)
    text = models.CharField()
    author = models.ForeignKey(get_user_model())
    created_date = models.DateTimeField()
    published_date = models.DateTimeField()

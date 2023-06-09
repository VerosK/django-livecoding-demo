from django.db import models


# Create your models here.
class Joke(models.Model):
    text = models.TextField(blank=False, null=False)
    pub_date = models.DateTimeField('date published')
    is_profane = models.BooleanField(default=False)

    def __str__(self):
        return self.text

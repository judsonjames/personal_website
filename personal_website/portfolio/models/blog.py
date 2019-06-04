from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=32, blank=False, null=False)
    published = models.DateTimeField()
    text = models.TextField()

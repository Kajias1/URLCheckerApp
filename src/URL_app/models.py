from django.db import models


class URLRecord(models.Model):
    id = models.AutoField(primary_key=True)
    url = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.url

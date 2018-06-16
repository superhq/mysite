from django.db import models


class Files(models.Model):
    path = models.CharField(max_length=1024)
    digest = models.CharField(max_length=256)

    def __str__(self):
        return self.path

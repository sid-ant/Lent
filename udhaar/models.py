from django.db import models

# Create your models here.

class Groups(models.Model):
    gid = models.IntegerField()
    uname = models.CharField(max_length=200)

    def __str__(self):
        return str(self.gid)

class Transactions(models.Model):
    gid = models.IntegerField()
    to  = models.CharField(max_length=200)
    from_user = models.CharField('from',max_length=200)
    amount = models.IntegerField()

    def __str__(self):
        return str(self.id)

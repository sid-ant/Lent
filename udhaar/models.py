from django.db import models

# Create your models here.

class Groups(models.Model):
    gid = models.IntegerField()
    uname = models.CharField(max_length=200)

class Transactions(models.Model):
    gid = models.ForeignKey(Groups, on_delete=models.CASCADE)
    to  = models.CharField(max_length=200)
    from_user = models.CharField('from',max_length=200)
    amount = models.IntegerField()

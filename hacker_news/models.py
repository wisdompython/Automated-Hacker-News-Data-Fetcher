from django.db import models
import re
import requests

# Create your models here
class Items(models.Model):
    id  = models.IntegerField(primary_key=True,unique=True)
    by = models.CharField(max_length=200, null=True, blank=True)
    type = models.CharField(max_length=200, null=True, blank=True)
    title = models.CharField(max_length=500, null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    descendants = models.IntegerField(null=True, blank=True)
    url = models.CharField(max_length=500, null=True, blank=True)
    deleted = models.BooleanField()
    dead = models.BooleanField()
    created =models.DateTimeField(auto_now_add=True)


class Comments(models.Model):
    id  = models.IntegerField(primary_key=True,unique=True)
    item = models.ForeignKey(Items,null=True, blank=True, on_delete=models.CASCADE)
    by = models.CharField(max_length=200, null=True, blank=True)
    type = models.CharField(max_length=200, null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    parent= models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='+')
    deleted = models.BooleanField()
    created =models.DateTimeField(auto_now_add=True)
    dead = models.BooleanField()

    class Meta:
        ordering = ('created',)

    @property
    def children(self):
        return Comments.objects.filter(parent=self,deleted=False, dead=False)    
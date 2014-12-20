from django.db import models
from urlparse import urlparse


class Poll(models.Model):
    auto_increment_id = models.AutoField(primary_key=True)
    Poll_Title = models.CharField(max_length=100, blank=False, null=False)
    Option1 = models.CharField(max_length=100)
    Option2 = models.CharField(max_length=100)
    Option3 = models.CharField(max_length=100, blank=True, null=True)
    Option4 = models.CharField(max_length=100, blank=True, null=True)
    Option5 = models.CharField(max_length=100, blank=True, null=True)

    Created_At = models.DateTimeField(auto_now_add=True)
    Updated_At = models.DateTimeField(auto_now=True)



    @property
    def domain(self):
        return urlparse(self.url).netloc

    def __unicode__(self):
        return self.Poll_Title


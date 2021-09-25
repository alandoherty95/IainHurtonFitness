from django.db import models


class ReceivedMessage(models.Model):

    class Meta:
        verbose_name = 'Message'

    name = models.CharField(max_length=40, null=False, blank=False)
    email = models.EmailField(max_length=50, null=False, blank=False)
    subject = models.CharField(max_length=254, null=False, blank=False)
    message = models.TextField(blank=False, null=False)
    date_sent = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

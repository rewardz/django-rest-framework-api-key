import uuid
from django.db import models
import re


class KeyOwner(models.Model):
    name = models.CharField(max_length=50, unique=True)
    # an RE that this api-key is validate for
    path_re = models.CharField(max_length=1024)

    def __str__(self):
        return self.name


class APIKey(models.Model):

    class Meta:
        verbose_name_plural = "API Keys"
        ordering = ['-created']

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    name = models.CharField(max_length=50, unique=True)
    old_key = models.CharField(max_length=40, unique=True)
    key = models.CharField(max_length=40, unique=True)
    owner = models.ForeignKey(KeyOwner, null=True)
    old_key_expiration_date = models.DateField(null=True, blank=True)
    expires_at = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name

    def is_valid(self, path):
        pattern = re.compile(self.owner.path_re)
        return pattern.search(path)


class ClientSecretKey(models.Model):
    class Meta:
        verbose_name_plural = "Client Secret Keys"
        ordering = ['-created']

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    name = models.CharField(max_length=50, unique=True)
    owner = models.ForeignKey(KeyOwner, null=True)
    secret_key = models.CharField(max_length=250, unique=True)
    old_secret_key = models.CharField(max_length=250, unique=True)
    old_key_expiration_date = models.DateField(null=True, blank=True)
    expires_at = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return self.name

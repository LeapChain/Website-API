import uuid

from django.core.cache import cache
from django.db import models
from thenewboston.models.created_modified import CreatedModified


class Feedback(CreatedModified):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    message = models.TextField()

    class Meta:
        verbose_name_plural = 'feedback'

    def save(self, *args, **kwargs):
        cache.delete_pattern('views.decorators.cache.cache*')
        return super(Feedback, self).save(*args, **kwargs)

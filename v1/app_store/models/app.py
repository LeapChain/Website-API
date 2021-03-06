import uuid

from django.core.cache import cache
from django.core.exceptions import ValidationError
from django.db import models
from thenewboston.models.created_modified import CreatedModified


class App(CreatedModified):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    logo = models.ImageField(upload_to='app_store')
    website = models.URLField()
    images = models.ManyToManyField('AppImage', blank=True, related_name='app_images')
    tagline = models.CharField(max_length=255, blank=True, null=True)
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    slug = models.CharField(max_length=255)
    page_hits = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'#{self.pk}: {self.name}'

    def validate_unique(self, *args, **kwargs):
        qs = App.objects.filter(slug=self.slug)
        if self.pk:
            qs = qs.exclude(pk=self.pk)
        if qs.count() > 0:
            raise ValidationError({'slug': ['App with similar slug already exists.']})

    def save(self, *args, **kwargs):
        self.validate_unique()
        cache.delete_pattern('views.decorators.cache.cache*')
        super(App, self).save(*args, **kwargs)

    def clean(self):
        if self.category is None:
            raise ValidationError({'category': ['This field is required.', ]})


class AppImage(CreatedModified):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    app = models.ForeignKey('App', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='app_store')

    def __str__(self):
        return f'#{self.pk}: {self.app} - {self.image}'

    def save(self, *args, **kwargs):
        cache.delete_pattern('views.decorators.cache.cache*')
        return super(AppImage, self).save(*args, **kwargs)


class Category(CreatedModified):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'categories'
        ordering = ('created_date',)

    def __str__(self):
        return f'#{self.pk}: {self.name}'

    def save(self, *args, **kwargs):
        cache.delete_pattern('views.decorators.cache.cache*')
        return super(Category, self).save(*args, **kwargs)

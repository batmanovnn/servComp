from django.db import models
from rest_framework.reverse import reverse


class Issue(models.Model):
    ind_orig = models.BooleanField
    ref_orig = models.IntegerField
    room_id = models.CharField(max_length=20, help_text="Enter field documentation")
    people_id = models.CharField(max_length=20, help_text="Enter field documentation")
    type_id = models.CharField(max_length=20, help_text="Enter field documentation")
    text = models.TextField(blank=True)
    worker_id = models.CharField(max_length=20, help_text="Enter field documentation")
    timestamp = models.DateTimeField(auto_now_add=True)    # Column(db.DateTime, index=True, default=datetime.utcnow)

    def __str__(self):
        return self.room_id

    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.id)])

    class Meta:
        ordering = ["-timestamp"]



class Post(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    body = models.TextField(blank=True, default='')
    owner = models.ForeignKey('auth.User', related_name='posts', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']


class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    body = models.TextField(blank=False)
    owner = models.ForeignKey('auth.User', related_name='comments', on_delete=models.CASCADE)
    post = models.ForeignKey('Post', related_name='comments', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']


class Category(models.Model):
    name = models.CharField(max_length=100, blank=False, default='')
    owner = models.ForeignKey('auth.User', related_name='categories', on_delete=models.CASCADE)
    posts = models.ManyToManyField('Post', related_name='categories', blank=True)

    class Meta:
        verbose_name_plural = 'categories'
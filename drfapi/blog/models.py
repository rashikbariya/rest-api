# from django.conf import settings
from django.db import models

def upload_posts_image(instance, filename):
    return "posts/{owner}/{filename}".format(owner=instance.owner, filename=filename)

# class PostsQuerySet(models.QuerySet):
#     pass

# class PostsManager(models.Manager):
#     def get_queryset(self):
#         return PostsQuerySet(self.model, using=self._db)

class Posts(models.Model):
    # user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    owner = models.ForeignKey('auth.User', related_name='posts', on_delete=models.CASCADE)
    content = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to=upload_posts_image, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    # objects = PostsManager()

    def __str__(self):
        return str(self.content)[:30]

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
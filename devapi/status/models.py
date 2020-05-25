import json
from  django.core.serializers import serialize
from django.db import models
from django.conf import settings
# Create your models here.

#serialize queryset
class StatusQuerySet(models.QuerySet):
    # def serialize(self):
    #     qs = self
    #     final_array = []
    #     for obj in qs:
    #         struct = json.loads(obj.serialize())
    #         final_array.append(struct)
    #     return json.dumps(final_array)
    
    def serialize(self):
        list_value = list(self.values("id","user","content"))
        return json.dumps(list_value)


class StatusManager(models.Manager):
    def get_queryset(self):
        return StatusQuerySet(self.model,using=self._db)

class Status(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = StatusManager() #linking StatusManager

    def __str__(self):
        return str(self.content)[:20]

    #serialize individual instance
    # def serialize(self):
    #     json_data =  serialize("json", [self], fields=('user','content'))
    #     struct = json.loads(json_data) #[{}] list of dict
    #     print(struct)
    #     data = json.dumps(struct[0]['fields'])
    #     return data
    def serialize(self):
        data = {
            "id": self.id,
            "user": self.user.id,
            "content": self.content,
        }
        data = json.dumps(data)
        return data

    class Meta:
        verbose_name = 'Status post'
        verbose_name_plural = 'Status posts'
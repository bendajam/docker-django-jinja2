from django.db import models
import uuid


class BaseModel(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    ctime = models.DateField(auto_now_add=True)
    mtime = models.DateField(auto_now=True)

    class Meta:
        abstract = True

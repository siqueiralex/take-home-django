import uuid
from django.db import models



class Question(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    question = models.TextField()
    answer = models.CharField(max_length=200)
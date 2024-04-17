import uuid
from django.db import models



class Question(models.Model):
    CATEGORY = (
        ('geography', 'Geography'),
        ('science', 'Science'),
    )
    
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    question = models.TextField()
    answer = models.CharField(max_length=200)
    category = models.CharField(
        max_length=100,
        choices=CATEGORY,
    )
    
    def check_answer(self, answer:str):
        return answer.strip().lower() == self.answer.strip().lower()
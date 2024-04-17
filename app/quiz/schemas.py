from ninja import Schema, ModelSchema
from .models import Question
from typing import Literal

class QuestionOut(ModelSchema):
    class Meta:
        model = Question
        fields = ['uuid', 'question', 'category']


class AnswerIn(Schema):
    question_uuid: str
    answer: Literal['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd']


class AnswerOut(Schema):
    answered_correctly: bool
    correct_answer: str


class ErrorSchema(Schema):
    message: str
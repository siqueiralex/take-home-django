from openai import OpenAI
from abc import ABC, abstractmethod
from typing import Literal
from .models import Question
import random


QuestionCategory = Literal['geography', 'science', 'random']


class QuestionGenerator(ABC):
    @abstractmethod
    def generate_question(self, category:QuestionCategory): ...



class GPTQuestionGenerator(QuestionGenerator):
    
    def generate_question(self, category:QuestionCategory) -> Question:
        # dealing with random
        if category == 'random':
            category_list = list(QuestionCategory.__args__)
            category_list.remove('random')
            category = random.choice(category_list)
        
        
        ## Call GPT
        
        return Question.objects.create(
            category = category,
            question = 'foo',
            answer = 'foo'
        )


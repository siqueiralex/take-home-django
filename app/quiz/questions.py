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
    
    def __init__(self, gpt_model = "gpt-3.5-turbo", gpt_temperature = .8) -> None:
        self.gpt_model = gpt_model
        self.gpt_temperature = gpt_temperature
        self.openai_client = OpenAI()
    
    def generate_question(self, category:QuestionCategory) -> Question:
        # dealing with random
        if category == 'random':
            category_list = list(QuestionCategory.__args__)
            category_list.remove('random')
            category = random.choice(category_list)
        
        
        system_message = '''
        You are an assistant to creating Quiz questions.
        You always create questions with 4 choices: A, B, C and D.
        The questions you create always have only one correct choice.
        Your response is always sent in the following structure:
        [Question Statement]
        A - Option A
        B - Option B
        C - Option C
        D - Option D
        Correct Answer: B
        '''
        
        response = self.openai_client.chat.completions.create(
            model = self.gpt_model,
            temperature = self.gpt_temperature,
            messages = [
                {'role' : 'system', 'content': system_message.strip()},
                {'role' : 'user', 'content': f"Create a simple question in the category: {category}"}
            ],
        )
        
        res_list = response.choices[0].message.content.split('Correct Answer:')
        question = res_list[0].strip()
        answer = res_list[1].strip()
        
        return Question.objects.create(
            category = category,
            question = question,
            answer = answer
        )

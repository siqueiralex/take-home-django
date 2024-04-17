from ninja import NinjaAPI
from django.core.handlers.wsgi import WSGIRequest

from .models import Question
from .schemas import AnswerIn, AnswerOut, QuestionOut, ErrorSchema
from .questions import QuestionCategory, GPTQuestionGenerator, QuestionGenerator


api = NinjaAPI()


@api.get("/question", response={200: QuestionOut, 500: ErrorSchema})
def get_question(request: WSGIRequest, category: QuestionCategory = 'random'):
    question_generator = GPTQuestionGenerator()
    
    try:
        question = question_generator.generate_question(category=category)
    except Exception as e:
        return 500, {'message': "Sorry. We're currently unable to generate a question for you."}
    
    return question


@api.post("/answer", response={200: AnswerOut, 404: ErrorSchema})
def answer(request: WSGIRequest, answer: AnswerIn):
    try:
        question = Question.objects.get(uuid=answer.question_uuid)
    except Exception as e:
        return 404, {'message': f"Sorry. We couldn't find a question with the uuid {answer.question_uuid}."}
    
    return { 
        'answered_correctly' : question.check_answer(answer=answer.answer),
        'correct_answer' : question.answer
    }
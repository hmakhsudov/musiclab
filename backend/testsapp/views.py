from django.shortcuts import render
from rest_framework import generics
from rest_framework.exceptions import NotFound

from .models import Test, TestTextQuestion, TestAnswer, UserTestAnswer
from .serializers import TestsSerializer, TestTextQuestionSerializer, TestAnswerSerializer, UserTestAnswerSerializer

class TestAPIList(generics.ListAPIView):
   queryset = Test.objects.all()
   serializer_class = TestsSerializer

class TestAPIRetrieve(generics.RetrieveAPIView):
    queryset = Test.objects.all()  # Определяем набор объектов для запроса
    serializer_class = TestsSerializer
    lookup_field = 'id'  # Устанавливаем ожидаемое имя URL параметра для идентификации объекта

   
class TestTextQuestionDetailView(generics.RetrieveAPIView):
    serializer_class = TestTextQuestionSerializer

    def get_queryset(self):
        test_id = self.kwargs.get('test_id')
        return TestTextQuestion.objects.filter(test_id=test_id)

    def get_object(self):
        queryset = self.get_queryset()
        question_index = self.kwargs.get('question_index')
        try:
            # Пытаемся получить вопрос по индексу
            question = queryset.get(question_index=question_index)
            return question
        except TestTextQuestion.DoesNotExist:
            # Если вопрос не найден, выбрасываем исключение NotFound
            raise NotFound('Вопрос не найден')
         

class TestAnswerListView(generics.ListAPIView):
    serializer_class = TestAnswerSerializer

    def get_queryset(self):
        question_id = self.kwargs.get('question_id')
        try:
            # Получаем все ответы на вопрос с указанным ID
            queryset = TestAnswer.objects.filter(question_id=question_id)
            return queryset
        except TestAnswer.DoesNotExist:
            # Если вопрос не найден, выбрасываем исключение NotFound
            raise NotFound('Ответы на вопрос не найдены')
         
   
class UserTestAnswerCreateView(generics.CreateAPIView):
    queryset = UserTestAnswer.objects.all()
    serializer_class = UserTestAnswerSerializer
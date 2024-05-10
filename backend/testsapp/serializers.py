from rest_framework import serializers
from .models import Test, Genre, TestTextQuestion, TestAnswer, UserTestAnswer

class TestsSerializer(serializers.ModelSerializer):
    genre_name = serializers.SerializerMethodField()  # Новое кастомное поле
    questions_count = serializers.SerializerMethodField()  # Новое кастомное поле

    class Meta:
        model = Test
        fields = ['id', 'title', 'testtype', 'genre_name', 'questions_count']  # Добавляем новое поле
        
        
    def get_genre_name(self, obj):
        return obj.genre.name  # Предполагается, что у вас есть модель Genre, и у нее есть поле name
    
    def get_questions_count(self, obj):
        return obj.get_questions_count()  # Используем метод для расчета количества вопросов
    
    
class TestTextQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestTextQuestion
        fields = ['id', 'test', 'question_index', 'fragment']


class TestAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestAnswer
        fields = ['id', 'question', 'is_correct', 'is_choice', 'answer_text']


class UserTestAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTestAnswer
        fields = ['user', 'test_question', 'chosen_answer']

    
class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['name']  # Замените 'name' на поле, которое содержит название жанра в вашей модели Genre
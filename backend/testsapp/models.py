from django.db import models
from django.utils.translation import gettext_lazy as _
from myauth.models import CustomUser

class Genre(models.Model):
    name = models.CharField(_("Название жанра"), max_length=50)
    photo = models.ImageField(_(""), upload_to='genre_images/', null=True, blank=True)
    def __str__(self):
        return self.name

class Test(models.Model):
    TEST_TYPES = (
        ('Тексты песен', 'Тексты песен'),
        ('Факты', 'Факты'),
        ('Знание песен', 'Знание песен'),
        ('Смешанное', 'Смешанное'),
    )
    title = models.CharField(_("Название"), max_length=220)
    genre = models.ForeignKey('Genre', verbose_name=_("Жанр"), on_delete=models.CASCADE)
    # questions_number = models.IntegerField(_("Количество вопросов"))
    testtype = models.CharField(_("Тип теста"), max_length=20, choices=TEST_TYPES)
    
    def __str__(self):
        return self.title
    
    def get_questions_count(self):
        return self.questions.count() if hasattr(self, 'questions') else 0  # Возвращает количество вопросов или 0, если вопросы не определены
    

class TestTextQuestion(models.Model):
    test = models.ForeignKey(Test, related_name='questions', on_delete=models.CASCADE)
    question_index = models.IntegerField(_("Номер вопроса"))
    fragment = models.TextField(_("Фрагмент песни"))
    
    def __str__(self):
        return f"Номер вопроса {self.question_index}, Тест - {self.test}, Вопрос: {self.fragment}"
    

class TestAnswer(models.Model):
    QUESTION_CHOICES = [(i, str(i)) for i in range(1, 5)]  # Четыре вариантов ответа
    question = models.ForeignKey(TestTextQuestion, related_name='answers', on_delete=models.CASCADE)
    is_correct = models.BooleanField(_("Правильный ответ"), default=False)
    is_choice = models.BooleanField(_("Выбранный ответ"), default=False)
    answer_text = models.CharField(_("Текст ответа"), max_length=255)
    
    
    def __str__(self):
        return f"{self.question}, Текст ответа - {self.answer_text}, Правильно: {self.is_correct}"


class UserTestAnswer(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='test_answers')
    test_question = models.ForeignKey(TestTextQuestion, on_delete=models.CASCADE, related_name='user_answers')
    chosen_answer = models.ForeignKey(TestAnswer, on_delete=models.CASCADE, related_name='chosen_by_user')
    # Другие поля, которые вам могут понадобиться, например, дата и время ответа

    def __str__(self):
        return f"Ответ пользователя {self.user.username} на вопрос {self.test_question.question_index} теста {self.test_question.test.title}"

class TestMusicQuestion(models.Model):
    pass
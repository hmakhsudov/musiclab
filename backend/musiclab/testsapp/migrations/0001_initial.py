# Generated by Django 5.0.4 on 2024-05-07 13:17

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название жанра')),
                ('photo', models.ImageField(upload_to='genre_images/', verbose_name='')),
            ],
        ),
        migrations.CreateModel(
            name='TestMusicQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=220, verbose_name='Название')),
                ('testtype', models.CharField(choices=[('Тексты песен', 'Тексты песен'), ('Факты', 'Факты'), ('Знание песен', 'Знание песен'), ('Смешанное', 'Смешанное')], max_length=20, verbose_name='Тип теста')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testsapp.genre', verbose_name='Жанр')),
            ],
        ),
        migrations.CreateModel(
            name='TestTextQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_index', models.IntegerField(verbose_name='Номер вопроса')),
                ('fragment', models.TextField(verbose_name='Фрагмент песни')),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='testsapp.test')),
            ],
        ),
        migrations.CreateModel(
            name='TestAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_correct', models.BooleanField(default=False, verbose_name='Правильный ответ')),
                ('is_choice', models.BooleanField(default=False, verbose_name='Выбранный ответ')),
                ('answer_text', models.CharField(max_length=255, verbose_name='Текст ответа')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='testsapp.testtextquestion')),
            ],
        ),
        migrations.CreateModel(
            name='UserTestAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chosen_answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chosen_by_user', to='testsapp.testanswer')),
                ('test_question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_answers', to='testsapp.testtextquestion')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='test_answers', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

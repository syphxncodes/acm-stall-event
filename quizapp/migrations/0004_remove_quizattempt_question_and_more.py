# Generated by Django 5.1.1 on 2024-10-12 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0003_question_remove_quizattempt_question_number_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quizattempt',
            name='question',
        ),
        migrations.AddField(
            model_name='quizattempt',
            name='question_number',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]

# Generated by Django 4.1 on 2022-08-04 22:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_answer_starred_by_alter_question_starred_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='image',
        ),
    ]
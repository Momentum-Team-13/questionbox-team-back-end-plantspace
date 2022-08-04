# Generated by Django 4.1 on 2022-08-03 16:05

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_question_starred_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='starred_by',
            field=models.ManyToManyField(related_name='starred_questions', to=settings.AUTH_USER_MODEL),
        ),
    ]
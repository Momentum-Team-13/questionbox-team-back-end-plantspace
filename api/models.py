from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    def __str__(self):
        return self.username

    def __repr__(self):
        return f'<User username={self.username} pk={self.pk}>'


class BaseModel(models.Model):
    created_at = models.DateTimeField(db_index=True, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Question(BaseModel):

    # Question Categories
    HOUSE_PLANTS = 1
    OUTDOOR_PLANTS = 2
    VEGETABLES = 3
    QUESTION_CATEGORIES = [
        (HOUSE_PLANTS, 'House Plants'),
        (OUTDOOR_PLANTS, 'Outdoor Plants'),
        (VEGETABLES, 'Vegetables'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='questions')
    title = models.CharField(max_length=125)
    body = models.TextField(max_length=750)
    category = models.PositiveSmallIntegerField(choices=QUESTION_CATEGORIES, null=True, blank=True)
    starred_by = models.ManyToManyField(User, related_name='starred_questions', blank=True)

    def __str__(self):
        return f"{self.title} {self.body} {self.category}"


class Answer(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='answers')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    answer_body = models.TextField(max_length=750)
    starred_by = models.ManyToManyField(User, related_name='starred_answers', blank=True)
 
    def __str__(self):
        return f"{self.question}  -  {self.answer_body}"

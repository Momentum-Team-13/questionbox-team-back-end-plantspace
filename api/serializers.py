from rest_framework import serializers
from .models import Answer, User, Question


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username')


class QuestionSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    category = serializers.ReadOnlyField(source='question.category')

    class Meta:
        model = Question
        fields = "__all__"


class AnswerSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Answer
        fields = ('pk', 'user', 'answer_body')

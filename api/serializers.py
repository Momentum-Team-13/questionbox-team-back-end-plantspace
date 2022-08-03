from rest_framework import serializers
from .models import Answer, User, Question


class QuestionSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    category = serializers.SerializerMethodField()

    class Meta:
        model = Question
        fields = ('__all__')

    def get_category(self, obj):
        return obj.get_category_display()


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username')


class AnswerSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Answer
        fields = ('pk', 'user', 'answer_body', 'created_at')


class QuestionSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    category_name = serializers.SerializerMethodField()
    answers = AnswerSerializer(many=True, read_only=True)
    
    class Meta:
        model = Question
        fields = ('__all__')
    
    def get_category_name(self, obj):
        return obj.get_category_display()


class UserSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True, read_only=True)
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'questions', 'answers')


from rest_framework import serializers
from .models import Answer, User, Question


class AnswerSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    starred_by = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='username'
    )

    class Meta:
        model = Answer
        fields = ('pk', 'user', 'question', 'answer_body', 'starred_by', 'created_at')


class QuestionSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    category_name = serializers.SerializerMethodField()
    answers = AnswerSerializer(many=True, read_only=True)
    starred_by = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='username'
    )


    class Meta:
        model = Question
        fields = ('__all__')
    
    def get_category_name(self, obj):
        return obj.get_category_display()


class AnswerSerializer2(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Answer
        fields = ('pk', 'user', 'answer_body', 'questions', 'created_at')


class UserSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True, read_only=True)
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'questions', 'answers')


class StarSerializer(serializers.ModelSerializer):
    starred_by = serializers.ReadOnlyField(source='user.username')
    
    class Meta:
        model = Question
        fields = ('id', 'starred_by')

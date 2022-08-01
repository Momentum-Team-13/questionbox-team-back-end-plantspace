from rest_framework import serializers
from .models import Answer, User, Question


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username')


class QuestionSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    category = serializers.SerializerMethodField()
    
    class Meta:
        model = Question
        fields = ('__all__')
    
    def get_category(self, obj):
        return obj.get_category_display()


class AnswerSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Answer
        fields = ('pk', 'user', 'answer_body')


from django.shortcuts import get_object_or_404
from .models import User, Question, Answer
from .permissions import QuestionOwner
from .serializers import UserSerializer, QuestionSerializer, AnswerSerializer, AnswerSerializer2, StarSerializer
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView


#get all questions; creates read-only endpoint representing a collection of questions; unauthentiated users can access this feature
class QuestionListView(generics.ListAPIView):
    queryset = Question.objects.all().order_by('created_at')
    serializer_class = QuestionSerializer


#post new question; this provides create-only endpoint; user MUST be authenticated
class QuestionCreateView(generics.ListCreateAPIView):
    queryset = Question.objects.all().order_by('created_at')
    serializer_class = QuestionSerializer
    permission_class = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


#get question and post answer; creates endpoint allowing answer to be added for the question; user MUST be authenticated
class AnswerListCreateView(generics.ListCreateAPIView):
    serializer_class = AnswerSerializer2
    permission_class = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Answer.objects.filter(question_id=self.kwargs["pk"])

    def perform_create(self, serializer):
        question = get_object_or_404(Question, pk=self.kwargs.get('pk'))
        serializer.save(user=self.request.user, question=question)


#delete question - ONLY by author...regardless of answered or unanswered; if deleted, all associated answers should also be deleted; #permissions.IsOwner designed from Custom Permissions DRF docs
class QuestionDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_class = [QuestionOwner]


#get question detail view - creates read-only endpoint showing single instance of the model; authentication NOT required
class QuestionDetailView(generics.RetrieveAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


#get questions user asked and answers user submitted
class UserQuestionAndAnswerView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request):
        answers = request.user.answers.all()
        questions = request.user.questions.all()
        q_serializer = QuestionSerializer(questions, many=True)
        a_serializer = AnswerSerializer(answers, many=True)
    
        return Response({"questions": q_serializer.data, "answers":a_serializer.data})


class StarUnstarQuestionView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        user = self.request.user
        question = get_object_or_404(Question, pk=self.kwargs['pk'])
        user.starred_questions.add(question)
        serializer = QuestionSerializer(question, context={'request': request})
        return Response(serializer.data, status=201)

    def delete(self, request, *args, **kwargs):
        user = self.request.user
        question = get_object_or_404(Question, pk=self.kwargs['pk'])
        user.starred_questions.remove(question)
        serializer = QuestionSerializer(question, context={'request': request})
        return Response(serializer.data, status=204)

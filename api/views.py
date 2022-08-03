from django.shortcuts import get_object_or_404
from .serializers import UserSerializer, QuestionSerializer, QuestionAndAnswerSerializer 
from rest_framework import generics, permissions
from .permissions import IsOwner
from .models import User, Question, Answer
from rest_framework.response import Response
from rest_framework.views import APIView


#get all questions; creates read-only endpoint representing a collection of questions; unauthentiated users can access this feature
class QuestionListView(generics.ListAPIView):
    queryset = Question.objects.all().order_by("created_at")
    serializer_class = QuestionSerializer


#post new question; this provides create-only endpoint; user MUST be authenticated
class QuestionCreateView(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_class = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


#get question and post answer; creates endpoint allowing answer to be added for the question; user MUST be authenticated
class AnswerListCreateView(generics.ListCreateAPIView):
    serializer_class = QuestionAndAnswerSerializer
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
    permission_class = [permissions.IsAuthenticated, IsOwner]


#get question detail view - creates read-only endpoint showing single instance of the model; authentication NOT required
class QuestionDetailView(generics.RetrieveAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionAndAnswerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

#get questions user asked and answers user submitted
class UserQuestionAndAnswerView(APIView):
    def get(self, request):
        serializer = UserSerializer(request.user)

        answers = request.user.answers
        questions = set([answer.question for answer in answers.all()])
        q_serializer = QuestionSerializer(questions, many=True)

        return Response({"questions asked by user": serializer.data, "answers given by user":q_serializer.data})

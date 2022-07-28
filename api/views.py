from .serializers import UserSerializer, QuestionSerializer, AnswerSerializer
from rest_framework import generics, permissions
# from .permissions import IsOwner
from .models import User, Question, Answer

# Create your views here.
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


#get all questions; creates read-only endpoint representing a collection of questions; unauthentiated users can access this feature
class QuestionListView(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


#post new question; this provides create-only endpoint; user MUST be authenticated
class QuestionCreateView(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_class = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


#get question and post answer; creates endpoint allowing answer to be added for the question; user MUST be authenticated
class AnswerQuestionView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_class = [permissions.IsAuthenticated]


#delete question - ONLY by author...regardless of answered or unanswered; if deleted, all associated answers should also be deleted; #permissions.IsOwner designed from Custom Permissions DRF docs
class QuestionDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_class = [permissions.IsAuthenticated] #permissions.IsOwner


#get question detail view - creates read-only endpoint showing single instance of the model; authentication NOT required
class QuestionDetailView(generics.RetrieveAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

# comment for PR purposes
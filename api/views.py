from .serializers import UserSerializer, QuestionSerializer
from rest_framework import generics, permissions
from .models import User, Question

# Create your views here.
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


#get all questions; this will provide read-only endpoint representing a collection of questions; unauthentiated users can access this feature
class QuestionListView(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

#post new question; this will provide create-only endpoint; MUST be authenticated; 
class QuestionCreateView(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_class = [permissions.IsAuthentiated]
from .serializers import CustomUserSerializer, QuestionSerializer
from rest_framework import generics, permissions
from .models import CustomUser, Question

# Create your views here.
class CustomUserList(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUser


#get all questions; this will provide read-only endpoint representing a collection of questions; unauthentiated users can access this feature
class QuestionListView(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

#post new question; this will provide create-only endpoint; MUST be authenticated; 
class QuestionCreateView(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_class = [permissions.IsAuthentiated]
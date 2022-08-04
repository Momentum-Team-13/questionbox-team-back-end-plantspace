from django.contrib import admin
from django.urls import path, include
from api import views as api_views
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('api/questions/', api_views.QuestionListView.as_view(), name='all_questions'),
    path('api/questions/new/', api_views.QuestionCreateView.as_view(), name='ask_new_question'),
    path('api/questions/<int:pk>/answer/', api_views.AnswerListCreateView.as_view(), name='answer_create'),
    path('api/answers/<int:pk>/star/', api_views.StarUnstarAnswerView.as_view(), name='star_unstar_answer'),
    path('api/questions/<int:pk>/details', api_views.QuestionDetailView.as_view(), name='question_details'),
    path('api/questions/<int:pk>/star/', api_views.StarUnstarQuestionView.as_view(), name='star_unstar_question'),
    path('api/questions/<int:pk>/trash', api_views.QuestionDeleteView.as_view(), name='delete_question'),
    path('api/myquestions/', api_views.UserQuestionAndAnswerView.as_view(), name='user_questions_and_answers'),
]

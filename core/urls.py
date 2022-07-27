"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from api import views as api_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('questions/', api_views.QuestionListView.as_view(), name='all_questions'),
    path('questions/new/', api_views.QuestionCreateView.as_view(), name='ask_new_question'),
    path('questions/<int:pk>/answer/<int:note_pk>', api_views.AnswerQuestionView.as_view(), name='answer_question'),
    path('questions/<int:pk>/details', api_views.QuestionDetailView.as_view(), name='question_details'),
    path('questions/<int:pk>/trash', api_views.QuestionDeleteView.as_view(), name='delete_question'),
]

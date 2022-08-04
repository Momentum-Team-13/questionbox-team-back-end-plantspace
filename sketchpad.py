class StarUnstarQuestion(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = StarSerializer
    permission_classes = [permissions.IsAuthenticated]

    def star_unstar_question(request):
        question = Question.objects.get(pk=request.id)
        user = request.user

        question.toggle_starred_by(instance=user) # User will be added


# Example from Docs
article = Article.objects.create(...)
publication = Publication.objects.create(...)

article.toggle_publications(instance=publication) # Will be added
article.toggle_publications(instance=publication) # Will be removed
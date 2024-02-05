from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from first_api.serializer import ArticleSerializer
from test_api.models import Article
from rest_framework.response import Response


class ArticleView(ModelViewSet):
    serializer_class = ArticleSerializer

    def get_queryset(self,*args,**kwargs):
        queryset=Article.objects.all()
        return queryset

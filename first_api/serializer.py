from rest_framework import serializers
from test_api.models import Article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['name','quantity','customer']
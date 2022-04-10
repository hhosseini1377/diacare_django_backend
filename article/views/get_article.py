from typing import Optional

from rest_framework.generics import RetrieveAPIView

from article.models import Article
from article.serializers import GetArticleSerializer


class GetArticleView(RetrieveAPIView):
    permission_classes = []
    authentication_classes = ()
    serializer_class = GetArticleSerializer
    queryset = Article.objects.all()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.instance = None  # type: Optional[Article]

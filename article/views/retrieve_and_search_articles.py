from typing import Optional

from django.db.models import Q
from django_plus.api import UrlParam as _p
from rest_framework.generics import ListAPIView
from rest_framework.pagination import LimitOffsetPagination

from article.models import Article
from article.serializers import GetArticleSerializer


class ListAndSearchArticles(ListAPIView):
    permission_classes = []
    authentication_classes = ()
    serializer_class = GetArticleSerializer
    pagination_class = LimitOffsetPagination

    list_params_template = [
        _p('tags', _p.list()),
        _p('subject', _p.string)
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.instance = None  # type: Optional[Article]

    def get_queryset(self):
        _q = Q()
        _query = Article.objects.all()
        tags_list = _p.clean_data(self.request.query_params, self.list_params_template)['tags']
        subject = _p.clean_data(self.request.query_params, self.list_params_template)['subject']
        if tags_list:
            _q |= Q(tags__name__in=tags_list)
        if subject:
            _q |= Q(subject__icontains=subject)

        return Article.objects.filter(_q).distinct()

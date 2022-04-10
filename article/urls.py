from django.urls import path

from article.views import (
    ListAndSearchArticles,
    GetArticleView
)

app_name = 'article'

urlpatterns = [
    path('retrieve/', ListAndSearchArticles.as_view(), name="retrieve-articles"),
    path('show/<int:pk>/', GetArticleView.as_view(), name='show-article'),
]

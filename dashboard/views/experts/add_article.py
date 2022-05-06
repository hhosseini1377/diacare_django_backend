from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from article.models import Article
from _helpers.custom_permisions import IsDoctor


class AddArticle(APIView):
    permission_classes = [IsDoctor, ]

    def post(self, request):
        context = request.data['context']
        subject = request.data['subject']
        try:
            Article.objects.create(context=context, subject=subject, writer=request.user)
            return Response({'message': 'مقاله اضافه شد'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message': 'شما قادر به انجام این عمل نیستید'}, status=status.HTTP_400_BAD_REQUEST)

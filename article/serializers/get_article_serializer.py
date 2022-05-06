import base64

from django.core.files import File
from rest_framework import serializers

from article.models import Tag, Article


class TagSerializer(serializers.RelatedField):
    class Meta:
        model = Tag

    def to_representation(self, value):
        return value.name


class GetArticleSerializer(serializers.ModelSerializer):
    thumbnail = serializers.SerializerMethodField()
    tags = TagSerializer(many=True, read_only=True)
    writer = serializers.CharField(read_only=True)

    class Meta:
        model = Article
        fields = ['id','thumbnail', 'subject', 'context', 'writer', 'tags']
        read_only_fields = ['subject', 'context', 'id']
        extra_fields = ['thumbnail', 'tags', 'writer']

    def get_writer(self, obj):
        return obj.writer.__str__()

    def get_thumbnail(self, obj):
        f = open(obj.thumbnail.path, 'rb')
        image = File(f)
        return base64.b64encode(image.read())

    def to_representation(self, instance):
        ret = super(GetArticleSerializer, self).to_representation(instance)
        ret['role'] = getattr(instance, 'writer').role
        return ret

    # def to_representation(self, instance):
    #     ret = OrderedDict()
    #     fields = self.Meta.read_only_fields
    #     for field in fields:
    #         ret[field] = getattr(instance, field)
    #     tags = getattr(instance, 'tags')
    #     ret['writer'] = getattr(instance, 'writer').__str__()
    #     ret['tags'] = tags.values_list('name', flat=True)
    #     ret['thumbnail'] = self.get_thumbnail(instance)
    #     return ret

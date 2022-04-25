from rest_framework import serializers

from free_diet.models import FreeDietInstance, FreeDietTemplatePart


class FreeDietPartsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FreeDietTemplatePart
        fields = ['week_day', 'meal', 'context']


class FreeDietInstanceAbstractSerializer(serializers.ModelSerializer):
    duration = serializers.CharField(source='free_diet.diet_period')
    kind = serializers.CharField(source='free_diet.free_diet_kind')
    name = serializers.CharField(source='free_diet.name')
    started_at = serializers.CharField(read_only=True)

    class Meta:
        model = FreeDietInstance
        fields = ['id', 'name', 'kind', 'duration', 'started_at']


class FreeDietInstanceSerializer(serializers.ModelSerializer):
    duration = serializers.CharField(source='free_diet.diet_period')
    kind = serializers.CharField(source='free_diet.free_diet_kind')
    name = serializers.CharField(source='free_diet.name')
    started_at = serializers.CharField(read_only=True)
    context = FreeDietPartsSerializer(many=True, source='free_diet.freediettemplatepart_set')

    class Meta:
        model = FreeDietInstance
        fields = ['name', 'kind', 'duration', 'started_at', 'context']

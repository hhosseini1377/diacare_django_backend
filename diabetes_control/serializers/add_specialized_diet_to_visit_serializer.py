from django.core.exceptions import ValidationError
from django.db import transaction
from rest_framework import serializers

from diabetes_control.models import SpecializedDiet, DietTemplatePart


class DietPartsSerializer(serializers.ModelSerializer):
    محتوا = serializers.CharField(source='context')
    روز = serializers.CharField(source='week_day')
    وعده = serializers.CharField(source='meal')

    class Meta:
        model = DietTemplatePart
        fields = ['روز', 'وعده', 'محتوا']


class SpecializedDietSerializer(serializers.ModelSerializer):
    diet_parts = DietPartsSerializer(many=True, source='diettemplatepart_set')

    class Meta:
        model = SpecializedDiet
        fields = ['name', 'diet_parts', 'visit']

    def create(self, validated_data):
        specialized_diet_data = {
            'name': validated_data['name'],
            'visit': validated_data['visit']
        }
        with transaction.atomic():
            try:
                specialized_diet = SpecializedDiet.objects.create(**specialized_diet_data)
            except ValidationError as e:
                raise serializers.ValidationError(*e)
        diet_parts = validated_data['diettemplatepart_set']
        for diet_part in diet_parts:
            diet_part_to_create = {
                'context': diet_part.get('context'),
                'meal': diet_part.get('meal'),
                'week_day': diet_part.get('week_day'),
                'specialized_diet': specialized_diet

            }
            with transaction.atomic():
                try:
                    DietTemplatePart.objects.create(**diet_part_to_create)
                except ValidationError as e:
                    raise serializers.ValidationError(*e)
        return specialized_diet

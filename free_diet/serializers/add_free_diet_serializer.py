from rest_framework import serializers

from free_diet.models import FreeDiet, FreeDietInstance


class AddFreeDietSerializer(serializers.ModelSerializer):
    class Meta:
        model = FreeDietInstance
        fields = ['free_diet']

    def create(self, validated_data):
        instance = FreeDietInstance.objects.create(
            free_diet=validated_data['free_diet'],
            account=self.context['request'].user
        )
        instance.save()
        return instance

    def to_representation(self, instance):
        ret = super(AddFreeDietSerializer, self).to_representation(instance)
        ret['resp'] = "رژیم رایگان موردنظر به داشبورد شما اضافه شد."
        return ret

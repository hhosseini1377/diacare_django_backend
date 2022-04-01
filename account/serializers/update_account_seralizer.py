from rest_framework import serializers
from django.contrib.auth import get_user_model
User = get_user_model()


class AccountUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'avatar']
        read_only_fields = ['pk', 'email', 'phone']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def update(self, instance, validated_data):
        if self.context['request'].user.pk != instance.pk:
            raise serializers.ValidationError({"authorize": "You dont have permission for this user."})
        instance.first_name = validated_data['first_name']
        instance.last_name = validated_data['last_name']
        return super(AccountUpdateSerializer, self).update(instance, validated_data)

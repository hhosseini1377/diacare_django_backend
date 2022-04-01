from rest_framework import serializers

from account.models import Account


class AccountPictureUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['pk', 'avatar']
        read_only_fields = ['pk']

    def update(self, instance, validated_data):
        return super(AccountPictureUpdateSerializer, self).update(instance, validated_data)

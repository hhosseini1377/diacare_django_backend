from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

User = get_user_model()


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True, write_only=True)
    new_password = serializers.CharField(required=True, write_only=True, validators=[validate_password])
    confirm_new_password = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = User
        fields = ('old_password', 'new_password', 'confirm_new_password')

    def validate(self, attrs):
        if attrs['new_password'] != attrs['confirm_new_password']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError({"old password": "Old password is not correct"})
        return value

    def update(self, instance, validated_data):
        if self.context['request'].user.pk != instance.pk:
            raise serializers.ValidationError({"authorize": "You dont have permission for this user."})
        instance.set_password(validated_data['new_password'])
        instance.save()

        return instance

    def to_representation(self, instance):
        ret = super(ChangePasswordSerializer, self).to_representation(instance)
        ret['response'] = "رمزعبور تغییر کرد"
        ret['user'] = getattr(instance, 'email')
        return ret

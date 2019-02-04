from rest_framework import serializers
from tasker.models import User, Task, Team, Comment

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'date_joined ', 'username')

    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get(instance.name)
        instance.created = validated_data.get(instance)
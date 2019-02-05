from rest_framework import serializers
from tasker.models import User, Task, Team, Comment

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'date_joined', 'username')

    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('username', instance.name)
        instance.created = validated_data.get('date_joined', instance.created)
        instance.save()
        return instance
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'name', 'created', 'creator', 'finished')

    def create(self, validated_data):
        return Task.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.created = validated_data.get('created', instance.created)
        instance.creator = validated_data.get('creator', instance.creator)
        instance.finished = validated_data.get('finished', instance.finished)
        instance.save()
        return instance
class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ('id', 'created', 'creator', 'name', 'users')

    def create(self, validated_data):
        return Team.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.created = validated_data.get('created', instance.created)
        instance.creator = validated_data.get('creator', instance.creator)
        instance.users = validated_data.get('users', instance.users)
        instance.save()
        return instance

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'comment', 'who_commented', 'commented')

    def create(self, validated_data):
        return Comment.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.comment = validated_data.get('comment', instance.comment)
        instance.who_commented = validated_data.get('who_commented', instance.who_commented)
        instance.commented = validated_data.get('commented', instance.commented)
        instance.save()
        return instance




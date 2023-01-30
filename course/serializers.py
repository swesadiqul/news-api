from rest_framework import serializers
from .models import *


class CourseSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=20)
    author = serializers.CharField(max_length=40)
    price = serializers.IntegerField()
    discount = serializers.IntegerField(default=0)
    duration = serializers.FloatField()

    def create(self, validated_data):
        return Course.objects.create(**validated_data)

    def update(self, course, validated_data):
        update_data = Course(**validated_data)
        update_data.id = course.id
        update_data.save
        return update_data
        
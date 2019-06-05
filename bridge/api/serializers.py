import logging

from rest_framework import serializers
from django.db import models
from api.models import Record, Keyword, Author
from pprint import pprint as pp
from django.core.exceptions import ValidationError


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ("name",)

    def to_representation(self, data):
        return data.name

    def to_internal_value(self, data):
        if not isinstance(data, str):
            raise serializers.ValidationError(f"'{data}' is not a string")
        return data


class KeywordListSerializer(serializers.Field):
    child = serializers.CharField()

    def to_representation(self, data):
        return [d["word"] for d in data.values()]

    def to_internal_value(self, data):
        if not isinstance(data, list):
            raise serializers.ValidationError(f"'{data}' is not a list")
        for d in data:
            if not isinstance(d, str):
                raise serializers.ValidationError(f"'{d}' is not a string")
        return data


class RecordSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    platform = serializers.CharField()
    keywords = KeywordListSerializer()

    class Meta:
        model = Record
        fields = ("posted", "author", "platform", "keywords")

    def create(self, validated_data):
        word_data = validated_data.pop("keywords")
        author = validated_data.pop("author")

        a, created = Author.objects.get_or_create(name=author)
        if created:
            a.save()

        record = Record.objects.create(author=a, **validated_data)

        words = []
        for w in word_data:
            word, created = Keyword.objects.get_or_create(word=w)
            if created:
                word.save()
            words.append(word)

        record.keywords.add(*words)
        return record

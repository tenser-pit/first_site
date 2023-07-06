from rest_framework import serializers
from rest_framework.renderers import JSONRenderer

from .models import Products

# TODO доделать - переделать serializer
class CategoryModel:
    def __init__(self, name):
        self.name = name


class CategorySerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=255)


def encode():
    model = CategoryModel('aasaasd')
    model_sr = CategorySerializer(model)
    json = JSONRenderer.render(model_sr.data)



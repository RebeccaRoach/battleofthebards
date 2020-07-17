from rest_framework import serializers
from game.models import Poem, Question, Clue

# TODO: USE HYPERLINKED Model Serializers to reflect relationships between entities in browsable API
# class HeroSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Hero
#         fields = ('name', 'alias')

class QuestionSerializer(serializers.ModelSerializer):
  class Meta:
   model = Question
   # grabs all the fields from model
   exclude = []

class PoemSerializer(serializers.ModelSerializer):
  class Meta:
   model = Poem
   exclude = []

class ClueSerializer(serializers.ModelSerializer):
  class Meta:
   model = Clue
   exclude = []
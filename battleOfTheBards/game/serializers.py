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
  #  exclude = []
   fields = ['text', 'score', 'answers']
  # need to add clues??

class PoemSerializer(serializers.ModelSerializer):
  questions = QuestionSerializer(many=True, read_only=True)

  class Meta:
    model = Poem
  #  exclude = []
    fields = ['title', 'author', 'year', 'text', 'questions']
  # need to add questions??
    



class ClueSerializer(serializers.ModelSerializer):
  class Meta:
   model = Clue
   exclude = []
   fields = ['text']
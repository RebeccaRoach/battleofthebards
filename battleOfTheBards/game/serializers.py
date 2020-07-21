from rest_framework import serializers
from game.models import Poem, Question, Clue

class ClueSerializer(serializers.ModelSerializer):
  class Meta:
   model = Clue
   fields = ['url', 'text']

class QuestionSerializer(serializers.ModelSerializer):
  clues = ClueSerializer(many=True, read_only=True)

  class Meta:
   model = Question
   fields = ['url', 'text', 'score', 'answers', 'clues']

class PoemSerializer(serializers.ModelSerializer):
  questions = QuestionSerializer(many=True, read_only=True)

  class Meta:
    model = Poem
    fields = [ 'url', 'title', 'author', 'year', 'text', 'questions']
    
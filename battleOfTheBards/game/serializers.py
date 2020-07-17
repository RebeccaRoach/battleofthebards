from rest_framework import serializers
from game.models import Poem, Question, Clue

class ClueSerializer(serializers.ModelSerializer):
  # url = serializers.HyperlinkedIdentityField(
  #   view_name='clue-detail',
  #   lookup_field='id'
  # )

  class Meta:
   model = Clue
  #  exclude = []
   fields = ['url', 'text']

class QuestionSerializer(serializers.ModelSerializer):
  clues = ClueSerializer(many=True, read_only=True)

  class Meta:
   model = Question
   fields = ['url', 'text', 'score', 'answers', 'clues']
  # need to add clues??


# class AccountSerializer(serializers.HyperlinkedModelSerializer):
#     url = serializers.HyperlinkedIdentityField(
#         view_name='accounts',
#         lookup_field='slug'
#     )
#     users = serializers.HyperlinkedRelatedField(
#         view_name='user-detail',
#         lookup_field='username',
#         many=True,
#         read_only=True
#     )

#     class Meta:
#         model = Account
#         fields = ['url', 'account_name', 'users', 'created']

class PoemSerializer(serializers.ModelSerializer):
  questions = QuestionSerializer(many=True, read_only=True)

  class Meta:
    model = Poem
    fields = [ 'url', 'title', 'author', 'year', 'text', 'questions']
  # need to add questions??
    
# serializing means turning python objects into JSON
# deserializing is the opposite - need to do this first
# check for where to write script to process poem json


#  has many relationships specified here
from rest_framework import serializers
from game.models import Poem, Question, Clue, Answer

class QuestionSerializer(serializers.Serializer):
    # id = serializers.IntegerField(read_only=True)

    # poem = models.ForeignKey(Poem, on_delete=models.CASCADE)
    # text = models.CharField(max_length=1000)
    # point_value = models.IntegerField(default=0)
    # answered_correctly = models.BooleanField(default=False)

    poem = serializers.(Poem, on_delete=models.CASCADE)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    point_value = serializers.IntegerField
    answered_correctly = serializers.BooleanField
    text = serializers.ChoiceField(required=True)
    # style={'base_template': 'textarea.html'}

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance

# postgres db
# write seed script somewhere to json -> models in DB
# serializers to write and play with
# deployment 
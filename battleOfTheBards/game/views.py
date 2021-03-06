from django.shortcuts import render

from game.models import Poem, Question, Clue
from game.serializers import PoemSerializer, QuestionSerializer, ClueSerializer
from rest_framework import generics

from rest_framework import viewsets

class PoemViewSet(viewsets.ModelViewSet):
  queryset = Poem.objects.all()
  serializer_class = PoemSerializer

class QuestionViewSet(viewsets.ModelViewSet):
  queryset = Question.objects.all()
  serializer_class = QuestionSerializer

class ClueViewSet(viewsets.ModelViewSet):
  queryset = Clue.objects.all()
  serializer_class = ClueSerializer

# class PoemList(generics.ListCreateAPIView):
#     queryset = Poem.objects.all()
#     serializer_class = PoemSerializer

# class PoemDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Poem.objects.all()
#     serializer_class = PoemSerializer

# class QuestionList(generics.ListCreateAPIView):
#     queryset = Question.objects.all()
#     serializer_class = QuestionSerializer

# class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Question.objects.all()
#     serializer_class = QuestionSerializer

# class ClueList(generics.ListCreateAPIView):
#     queryset = Clue.objects.all()
#     serializer_class = ClueSerializer

# class ClueDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Clue.objects.all()
#     serializer_class = ClueSerializer
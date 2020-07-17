from django.db import models
from django.contrib.postgres.fields import ArrayField

# TODO: Validations/ Permissions?

# Game model - do I really need this, or just Poem, Question, and Clue models??
# class Game(models.Model):
#   # to do top score, media ranker approach
#   start_time = models.DateTimeField(auto_now=True)
#   end_time = models.DateTimeField(auto_now=True)
#   score = models.IntegerField(default=0)
#   player_initials = models.CharField(max_length=25)

# Poem
class Poem(models.Model):
  # game = models.ForeignKey(Game)
  title = models.CharField(max_length=200)
  author = models.CharField(max_length=200)
  year = models.CharField(max_length=4)
  text = models.TextField()

  def __str__(self):
    return self.author + " - '" + self.title + "'"

# Question
class Question(models.Model):
  poem = models.ForeignKey(Poem, related_name='questions', on_delete=models.CASCADE)
  text = models.CharField(max_length=1000)
  score = models.IntegerField(default=0)
  answers = ArrayField(
    models.CharField(max_length=1000)
  )

  def __str__(self):
    return str(self.score) + " points - " + self.text

# Clue
class Clue(models.Model):
  question = models.ForeignKey(Question, on_delete=models.CASCADE)
  text = models.CharField(max_length=1000)

  def __str__(self):
    return "(" + str(self.question) + ") " + self.text
  
 # each model gets own endpoint, but most work on frontend
 #  API returns ids (poem 7 returns questions as list of IDs)
 #  API returns question ID, which could load up appropriate poem ID
 # OR simpler on the frontend: single request, load the big chunk of poem data, including all questions and clues
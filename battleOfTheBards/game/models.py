from django.db import models
from django.contrib.postgres.fields import ArrayField

# Poem
class Poem(models.Model):
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
  question = models.ForeignKey(Question, related_name='clues', on_delete=models.CASCADE)
  text = models.CharField(max_length=1000)

  def __str__(self):
    return "(" + str(self.question) + ") " + self.text
  
from django.db import models
# from django.contrib.postgres.fields import JSONField

# class Dog(models.Model):
#     name = models.CharField(max_length=200)
#     data = JSONField()

#     def __str__(self):
#         return self.name

# Dog.objects.create(name='Rufus', data={
# ...     'breed': 'labrador',
# ...     'owner': {
# ...         'name': 'Bob',
# ...         'other_pets': [{
# ...             'name': 'Fishy',
# ...         }],
# ...     },
# ... })
# >>> Dog.objects.create(name='Meg', data={'breed': 'collie', 'owner': None})

# >>> Dog.objects.filter(data__breed='collie')
# <QuerySet [<Dog: Meg>]>

# Game model - do I really need this, or just Poem, Question, and Clue models??
class Game(models.Model):
  # to do top score, media ranker approach
  start_time = models.DateTimeField(auto_now=True)
  end_time = models.DateTimeField(auto_now=True)
  score = models.IntegerField(default=0)
  player_initials = models.CharField(max_length=25)

# Poem
class Poem(models.Model):
  # game = models.ForeignKey(Game)
  title = models.CharField(max_length=200)
  author = models.CharField(max_length=200)
  date = models.CharField(max_length=4)
  text = models.TextField

# Question
class Question(models.Model):
  poem = models.ForeignKey(Poem, on_delete=models.CASCADE)
  text = models.CharField(max_length=1000)
  point_value = models.IntegerField(default=0)
  answered_correctly  = models.BooleanField(default=False)

class Answer(models.Model):
  question = models.ForeignKey(Question, on_delete=models.CASCADE)
  text = models.CharField(max_length=1000)

# Clue
class Clue(models.Model):
  question = models.ForeignKey(Question, on_delete=models.CASCADE)
  text = models.CharField(max_length=1000)
  

 # each model gets own endpoint, but most work on frontend
 #  API returns ids (poem 7 returns questions as list of IDs)
 #  API returns question ID, which could load up appropriate poem ID
 # OR simpler on the frontend: single request, load the big chunk of poem data, including all questions and clues
import json 
from game.models import Poem, Question, Clue

with open('game/poem_data.json', 'r') as json_file:
  poem_data = json.loads(json_file.read())
  for p in poem_data:
    questions = p.pop("questions")
    poem = Poem(**p)
    poem.save()

    for q in questions:
      q['poem_id'] = poem.id
      clues = q.pop("clues")
      question = Question(**q)
      question.save()

      for c in clues:
        c['question_id'] = question.id
        clue = Clue(**c)
        clue.save()
  
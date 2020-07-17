from django.contrib import admin

from .models import Poem, Question, Clue
admin.site.register(Poem)
admin.site.register(Question)
admin.site.register(Clue)
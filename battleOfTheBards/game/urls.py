from django.urls import path
# from rest_framework.urlpatterns import format_suffix_patterns
from game import views

# urlpatterns = [
#     # need to define an index view?
#     # path('', views.index, name='index'),
#     path('poems/', views.PoemList.as_view()),
#     path('poems/<int:pk>/', views.PoemDetail.as_view()),
#     path('questions/', views.QuestionList.as_view()),
#     path('questions/<int:pk>/', views.QuestionDetail.as_view()),
#     path('clues/', views.ClueList.as_view()),
#     path('clues/<int:pk>/', views.ClueDetail.as_view()),
# ]

from django.urls import include, path
from rest_framework import routers
# from . import views

router = routers.DefaultRouter()
router.register(r'poems', views.PoemViewSet)
router.register(r'questions', views.QuestionViewSet)
router.register(r'clues', views.ClueViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
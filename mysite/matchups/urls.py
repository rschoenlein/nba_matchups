from django.urls import path
from matchups.views import IndexView
from matchups.views import ResultsView


urlpatterns = [
    path('', IndexView.as_view(), name = 'index'),
    path('results', ResultsView.as_view(), name = 'results')
]

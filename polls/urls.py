
from django.urls import path
from . import views

app_name = "polls"
urlpatterns = [
    path('',views.IndexView , name="index"),
    path('<int:question_id>/', views.DetailsView , name="detail"),
    path('<int:question_id>/result', views.ResultsView , name="result"),
    path('<int:question_id>/vote', views.VotesView , name="vote"),
]

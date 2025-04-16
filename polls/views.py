from django.shortcuts import render ,get_object_or_404
from django.http import HttpResponse ,Http404

from .models import Question

# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list":latest_question_list}
    return render(request , "polls/index.html",context)

def details(request,question_id):
    question = get_object_or_404(Question, pk=question_id)       #we can use helper function as well
    return render(request, "polls/detail.html", {"question": question})  
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question not exist")
    # return render(request ,"polls/detail.html", {"question":question})

def results(request,question_id):
    return HttpResponse("you are looking results:%s. "%question_id)

def votes(request,question_id):
    return HttpResponse("you are looking votes:%s. "%question_id)


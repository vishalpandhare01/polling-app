from django.shortcuts import render ,get_object_or_404
from django.http import HttpResponse ,Http404 ,HttpResponseRedirect
from django.db.models import F
from django.urls import reverse
from django.views import generic

from .models import Question

# Create your views here.
def IndexView(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list":latest_question_list}
    return render(request , "polls/index.html",context)

def DetailsView(request,question_id):
    question = get_object_or_404(Question, pk=question_id)       #we can use helper function as well
    return render(request, "polls/detail.html", {"question": question})  
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question not exist")
    # return render(request ,"polls/detail.html", {"question":question})

def ResultsView(request,question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})

def VotesView(request,question_id):
    question = get_object_or_404(Question , pk=question_id)
    try:
       selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except:
        return render(
            request,
            "poll/detail.html",
            {
                "question":question,
                "error_message":"You didnt selected choice.",
            },
        )
        
    else:
       selected_choice.votes = F("votes") + 1
       selected_choice.save()
       # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
       return HttpResponseRedirect(reverse("polls:result", args=(question.id,)))


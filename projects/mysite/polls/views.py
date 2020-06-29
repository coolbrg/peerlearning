from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Question

def index(request):
  return HttpResponse("Namaste, World. You are at the polls index")

# ask yourself, where this question_id coming from?
def detail(request, question_id):
  question = get_object_or_404(Question, pk=question_id)
  return render(request, 'polls/detail.html', { 'question': question })

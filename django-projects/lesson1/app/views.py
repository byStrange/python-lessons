from django.shortcuts import render
from .models import *
from django.views.generic import ListView
from django.http import JsonResponse
import json
# Create your views here.


class HomeView(ListView):
    model = Quiz
    template_name = 'index.html'
    context_object_name = 'tests'


def __json(req):
    # if user requesting authenticated, return all quizzes with JSONResponse
    if req.user.is_authenticated:
        data = [{"numb": x.id, 'question': x.question, 'answer': x.answer, "options": x.options.replace(" ", "").split(',')}
                for x in Quiz.objects.all()]
        response = {
            "questions": data
        }
        return JsonResponse(response, safe=False)
    else:
        return JsonResponse({'error': 'You are not authenticated'})

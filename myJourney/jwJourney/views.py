from django.shortcuts import render
from .models import LearningMyJourney

# Create your views here
def index(request):
    journeys = LearningMyJourney.objects.all()
    return render(request, 'index.html', {'journeys': journeys})

def aboutMe(request):
    return render(request, 'aboutMe.html')
from django.shortcuts import render

# Create your views here.
from .models import Course


def index(request):
    courses = Course.objects.all()
    context = {
        'courses': courses
    }
    template_name = 'courses/index.html'
    return render(request, template_name, context)

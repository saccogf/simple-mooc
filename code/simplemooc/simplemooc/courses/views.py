from django.shortcuts import render, get_object_or_404
from .forms import ContactCourse

# Create your views here.
from .models import Course


def index(request):
    # Returns a list of all objects
    courses = Course.objects.all()
    context = {
        'courses': courses
    }
    template_name = 'courses/index.html'
    return render(request, template_name, context)


def details(request, slug):
    course = get_object_or_404(Course, slug=slug)
    context = {}
    if request.method == 'POST':
        form = ContactCourse(request.POST)
        if form.is_valid():
            context['is_valid'] = True
            form.send_email(course)
            form = ContactCourse()
    else:
        form = ContactCourse()
    context['course'] = course
    context['form'] = form

    template_name = 'courses/details.html'
    return render(request, template_name, context)


# def details(request, pk):
#     # Searches for object using ?<pk>, returns 404 if none is found
#     course = get_object_or_404(Course, pk=pk)  # (Object, filters)
#     context = {
#         'course': course
#     }
#     template_name = 'courses/details.html'
#     return render(request, template_name, context)

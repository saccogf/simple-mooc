from django.shortcuts import render

# Create your views here.


def register(request):
    template_name = 'accounts/register.html'
    return render(request, template_name)

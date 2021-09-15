from django.shortcuts import render

# Create your views here.
def basepage(request):
    return render(request, 'base.html')


def frontpage(request):
    return render(request, 'frontpage.html')
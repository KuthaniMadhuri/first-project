from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def propose(request):
    return HttpResponse('<h1><marquee> Harsha I Love u Bangaram<marquee><h1>')
def chinna(request):
    return HttpResponse('<h1><marquee>chinna Miss u ra bujji Bangaram<marquee><h1>')

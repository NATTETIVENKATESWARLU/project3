from django.shortcuts import render

# Create your views here.
def venkey(request):
    d={'a':20,'b':10}
    return render(request,'venkey.html',d)
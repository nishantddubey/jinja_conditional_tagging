from django.shortcuts import render

# Create your views here.
def conditions(request):
    d = {"a" : 23,"b" : 3}
    return render(request,'conditions.html',d)
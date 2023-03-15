from django.shortcuts import render

# Create your views here.
def conditions(request):
    d={'a':50,'b':100,'c':75}
    return render(request,'conditions.html',context=d)

def loops(request):
    d={'name':'Uma'}
    return render(request,'loops.html',d)
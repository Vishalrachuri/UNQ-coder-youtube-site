from django.shortcuts import render
from django.http import HttpResponse
from . models import Viedo,PlayList
def search(request):
    q=request.GET['query']
    playlists=PlayList.objects.all().filter(tags__icontains=q)
    return render(request,'search.html',{'playlists':playlists})

def playlist(request):
    playlists=PlayList.objects.all()
    return render(request,'vedios.html',{'playlists':playlists})

def home(request):
    #must return vedios which must be top 10 in vedios variable
    viedos=Viedo.objects.all().filter(istop=True)
    print(viedos[0].iframelink)
    return render(request,'home.html',{'viedos':viedos})

def viedo(request,playname,vno):
    n=len(Viedo.objects.all().filter(playname=playname))
    print(n)
    vedio=Viedo.objects.all().filter(playname=playname,vedioNumber=vno)[0];
    next=vno+1
    prev=vno-1
    if vno==1:
        prev=prev+1
    if vno==n:
        next=next-1
    print(vedio)
    return render(request,'v.html',{'vedio':vedio,'prev':prev,'next':next,'vno':vno,'n':n})
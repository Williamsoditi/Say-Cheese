from django.shortcuts import render
import datetime as dt
from django.http import Http404
from .models import Pictures, Location, Category
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
def home(request):
    Picture = Pictures.objects.all().order_by('-id')
    location = Location.objects.all()
    category = Category.objects.all()
    return render(request, 'all_pics/home.html',{'Picture':Picture,'location':location,'category':category})

def search_results(request):
    
    if 'pictures' in request.GET and request.GET["pictures"]:
        search_term = request.GET.get("pictures")
        searched_pictures = Pictures.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'all_pics/search.html',{"message":message,"pictures": searched_pictures})

    else:
        message = "You haven't searched for any category"
        return render(request, 'all_pics/search.html',{"message":message})

def pictures(request,pictures_id):
    try:
        pictures = Pictures.objects.get(id = pictures_id)
    except ObjectDoesNotExist:
        raise Http404()
    return render(request,"all_art/pictures.html", {"pictures":pictures})

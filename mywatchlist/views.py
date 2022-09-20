from django.shortcuts import render
from mywatchlist.models import WatchList
from django.http import HttpResponse
from django.core import serializers
from django.core import TemplateHTMLRenderer
from django.core import Response

# Create your views here.
def show_mywatchlist(request):
    return render(request, "mywatchlist.html", context)

data_movie_mywatchlist = WatchList.objects.all()
context = {
    'data_movies': data_movie_mywatchlist,
    'nama': 'Emily Rumia Naomi',
    'npm' : '2106652700',
}

class MySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("html_text",)

def show_html(request):
    data = WatchList.objects.all()
    return HttpResponse(serializers.serialize("fields", data), content_type="application/html")

def show_xml(request):
    data = WatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = WatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")



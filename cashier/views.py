from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def landingpage(request):
   return HttpResponse("<h2 style='color:blue;'>Hello, Ini Halaman Saya.</h2> </p> line ke dua <p> <img src='https://www.w3schools.com/html/pic_trulli.jpg' > " )


from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    data = {"header": "Homepage", "message": "Welcome to My site!"}
    return render(request, 'homepage.html', context = data)

def about(request):
    header = "About us";
    staff = ["Jhon", "Jhon2", "Jhon3"]
    director = {"name":"David", "img":"directors.png"}
    address = ["20 stiit", "NYork", "101010", "usa"]
    data = {"header": header, "staff": staff, "director": director, "address": address}
    return render(request, 'about.html', context = data)




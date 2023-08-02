from django.shortcuts import render


def index(request):

    return render(request, "customer/welcome.html", {"name": "Muzzammil", "title": "My web title"})

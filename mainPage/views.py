from django.shortcuts import render


def start(request):
    data = {
        'title': 'Main Page'
    }
    return render(request, "mainPage/start.html", data)


def about(request):
    return render(request, 'mainPage/about.html')


def contacts(request):
    return render(request, 'mainPage/contacts.html')

from django.shortcuts import render
from django.http import HttpResponseNotFound


def index(request):
    return render(request, 'index.html')


def submitquery(request):
    q = request.GET['query']
    try:
        answer = eval(q)
        mydict = {
            'q': q,
            'answer': answer,
            'error': False,
            'result': True
        }
        return render(request, 'index.html', context=mydict)
    except:
        mydict = {
            'error': True,
            'result': False
        }
        return render(request, 'index.html', context=mydict)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

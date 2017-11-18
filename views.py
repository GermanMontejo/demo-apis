from django.shortcuts import render
import requests
import json
from .forms import BookForm
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

BASE_URL = 'https://ueqv9hm43i.execute-api.ap-southeast-1.amazonaws.com/BooksProd'


def index(request):
    print("demo-apis index")
    return render(request, 'demo-apis/html/index.html')


def upsert_book(request):
    """ Adds a new book."""
    if request.method != 'POST':
        form = BookForm()
        context = {'data': form}
        return render(request, 'demo-apis/html/upsert_book.html', context)

    else:
        title = request.POST['title']
        author = request.POST['author']
        date_pub = request.POST['date_pub']

        url = BASE_URL + '/books'
        book = {'title': title, 'author': author, 'date_pub': date_pub}
        response = requests.post(url=url, json=book)
        print(response.json())
        return HttpResponseRedirect(reverse('demo_apis:get_all_books'))

def get_all_books(request):
    url = BASE_URL + '/books'
    resp = requests.get(url=url).json()
    print('resp: ' + json.dumps(resp['Items'], indent=4, sort_keys=True))
    context = {'books': resp['Items']}
    return render(request, 'demo-apis/html/all_books.html', context)


def get_book(request):
    if request.method == 'GET':
        print(request.GET)
        if 'title' in request.GET:
            title = {'title': request.GET['title']}
            print('title: ' + str(title))
            url = BASE_URL + '/books/title'
            response = requests.get(url=url, params=title)
            print("response: " + str(response.json()))
            context = {'book': response.json()}
            return render(request, 'demo-apis/html/book.html', context)

    return render(request, 'demo-apis/html/get_book.html')

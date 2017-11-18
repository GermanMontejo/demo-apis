from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^upsert-book/$', views.upsert_book, name='upsert_book'),
    url(r'^get-book/$', views.get_book, name='get_book'),
    url(r'^get-all-books/$', views.get_all_books, name='get_all_books')
]

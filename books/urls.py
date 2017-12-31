from django.conf.urls import url, include
from . import views
from rest_framework.routers import DefaultRouter
#
# urlpatterns = [
#     url(r'^$', views.book_list, name='book_list'),
#     url(r'^books/create/$', views.book_create, name='book_create'),
#     url(r'^books/(?P<pk>\d+)/update/$', views.book_update, name='book_update'),
#     url(r'^books/(?P<pk>\d+)/delete/$', views.book_delete, name='book_delete'),
# ]


router = DefaultRouter()
router.register(r'books', views.BookViewSet)

urlpatterns = [
    url(r'^', include(router.urls))
]

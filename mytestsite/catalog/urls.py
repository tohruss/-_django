from . import views
from django.urls import re_path
from .views import BBLogoutView, BBLoginView

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^books/$', views.BookListView.as_view(), name='books'),
    re_path(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
    re_path(r'authors/$', views.AuthorListView.as_view(),name='authors'),
    re_path(r'^authors/(?P<pk>\d+)$', views.AuthorDetailView.as_view(), name='author-detail'),
    re_path(r'accounts/login/$', BBLoginView.as_view(), name='login'),
    re_path(r'accounts/logout/$',BBLogoutView.as_view(), name='logout'),
    re_path(r'^mybooks/$', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
]
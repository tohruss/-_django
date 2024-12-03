from django.shortcuts import render
from .models import Book, BookInstance, Author, Genre
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LogoutView, LoginView


def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    # Генерация "количеств" некоторых главных объектов
    num_books = Book.objects.count()  # Общее количество книг
    num_instances = BookInstance.objects.count()  # Общее количество экземпляров книг
    num_instances_available = BookInstance.objects.filter(status='a').count()  # Доступные книги (статус = 'a')
    num_genres = Genre.objects.count()  # Общее количество жанров

    num_authors = Author.objects.count()  # Общее количество авторов
    num_visits = request.session.get('num_visits', 0)

    request.session['num_visits'] = num_visits + 1

    # Отрисовка HTML-шаблона index.html с данными внутри переменной контекста context
    return render(
        request,
        'index.html',
        context={
            'num_books': num_books,
            'num_instances': num_instances,
            'num_instances_available': num_instances_available,
            'num_authors': num_authors,
            'num_genres': num_genres,
            'num_visits': num_visits
        },
    )

class BookListView(generic.ListView):
    model = Book
    paginate_by = 2
    def get_queryset(self):
            return Book.objects.filter(title__icontains='')[:5] # Получить 5 книг, содержащих '' в заголовке



class BookDetailView(generic.DetailView):
    model = Book

class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 1
    def get_queryset(self):
            return Author.objects.all()

class AuthorDetailView(generic.DetailView):
    model = Author


class BBLoginView(LoginView):
   template_name = 'registration/login.html'

class BBLogoutView(LoginRequiredMixin, LogoutView):
   template_name = 'registration/logged_out.html'


class LoanedBooksByUserListView(LoginRequiredMixin,generic.ListView):
    """
    Generic class-based view listing books on loan to current user.
    """
    model = BookInstance
    template_name ='catalog/bookinstance_list_borrowed_user.html'


    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')

import pytest
from django.contrib.auth import get_user_model
from django.test.client import Client
from pytest_django import fixtures

from books.models import Book

User = get_user_model()


def test_is_it_working():
    assert True == 1

# def test_should_fail():
#     assert False == 1

def test_even_numer():
    number = 10
    assert number % 2 == 0

@pytest.mark.django_db
def test_create_user():
    user = User.objects.create_user(
        username='test1',
        password='password1',
    )
    assert user.username == 'test1'
    assert user.check_password('password1')

# fixture

@pytest.fixture
def user(db) -> User:
    u = User.objects.create_user(
        username='test1',
        password='password1',
    )
    return u

@pytest.fixture
def logged_in_client(user, client: Client) -> Client:

    # facem un browser simulat si logat care poate face requesturi HTTP
    client.login(
        username='test1',
        password='password1',
    )
    return client

@pytest.fixture
def book(user, logged_in_client):
    b = Book.objects.create(title='test-title', author='test-author', user=user)
    return b

def test_list_all_books(logged_in_client):
    # HTTP GET request:
    response = logged_in_client.get('/')
    assert response.status_code == 200

def test_does_book_exist(logged_in_client, book):
    # HTTP GET request:
    response = logged_in_client.get('/')
    assert response.status_code == 200
    assert "test-title" in str(response.context)

def test_user_book_count(user):
    book1 = Book.objects.create(title='test-title', author='test-author', user=user)
    book2 = Book.objects.create(title='test-title2', author='test-author2', user=user)
    books = list(Book.objects.filter(user_id=user.pk))
    assert len(books) == 2

def test_user_book_count_html(user, client):
    book1 = Book.objects.create(title="book 1", author="author 1", user=user)
    book2 = Book.objects.create(title="book 2", author="author 2", user=user)
    book3 = Book.objects.create(title="book 3", author="author 3", user=user)

    response = client.get("/")
    assert response.status_code == 200
    main_page_text = str(response.content)
    assert main_page_text.count(f"/user/{user.pk}/books/") == 3

def test_delete_book(user, book, logged_in_client: Client):
    # conceptual:
    # HTTP POST request pe url: /delete_book/{book.id}
    response = logged_in_client.post(f"/delete_book/{book.pk}/")
    assert response.status_code == 302

    response = logged_in_client.post(f"/delete_book/{book.pk}/")
    assert response.status_code == 404

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

# fixture
@pytest.fixture
def logged_in_client(db, client: Client) -> Client:
    user= User.objects.create_user(
        username='test1',
        password='password1',
    )
    # facem un browser simulat si logat care poate face requesturi HTTP
    client.login(
        username='test1',
        password='password1',
    )
    return client

@pytest.fixture
def book(db, logged_in_client):
    user = User.objects.create_user(
        username='test2',
        password='password2',
    )
    b = Book.objects.create(title='test-title', author='test-author', user='test-user')
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

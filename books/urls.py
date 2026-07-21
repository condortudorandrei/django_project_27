from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.list_books, name='home'),
    path("create_book/", views.create_book, name='create_book'),
    path("delete_book/<int:pk>/", views.delete_book, name='delete_book'),
    path("update_book/<int:pk>/", views.update_book, name='update_book'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
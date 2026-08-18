from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Book
from .serializers import BookSerializer

# ["GET"] -> ne spune ca acest view accepta doar HTTP GET request-uri
@api_view(["GET"])
def api_book_list(request):
    books = Book.objects.all().order_by("pk")
    serializer = BookSerializer(books, many=True, context={"request": request})
    return Response(serializer.data)


@api_view(["GET", "DELETE"])
def api_book_detail(request, pk):
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return Response({'detail': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'DELETE':
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    serializer = BookSerializer(book, context={"request": request})
    return Response(serializer.data)

from django.http import JsonResponse
from firstApi.models import Book
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from firstApi.serializer import BookSerializer


# Create your views here.
@api_view(['GET'])
def book_list(request):
    books = Book.objects.all()
    serializer = BookSerializer(books,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def book_create(request):
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    else:
        return Response(serializer.errors)

@api_view(['GET','PUT','DELETE'])

def book(request, pk):
    try:
        book = Book.objects.get(pk=pk)
    except:
        return Response({
            'error':'Books does not exists'
        },status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = BookSerializer(book)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = BookSerializer(book, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
      
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

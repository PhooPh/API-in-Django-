from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Book
import json


class BookApiView(APIView):

    def get(self,request):
        allBooks = Book.objects.all().values()
        return Response({'Messages':'listofbook','Book_List':allBooks})
# Modified ( Error Fixed Json )
    def post(self,request):
        try:
            # Try to parse JSON data from the request body
            json_data = json.loads(request.body.decode('utf-8'))
            book = Book.objects.create(id=json_data.get("id",None),
                                title=json_data.get("title",""),
                                author=json_data.get("author","")
                                )
            
           
            return Response({'Messages': 'new book added', 'Book_List': {'id': book.id, 'title': book.title, 'author': book.author}})
        
        except json.JSONDecodeError:
             return Response({'error': 'Invalid JSON data'}, status=status.HTTP_400_BAD_REQUEST)

# Original ( Not Fixed Error for Json )
    #def post(self,request):
        #Book.objects.create(id=request.data["id"],
                            #title=request.data["title"],
                            #author=request.data["author"]
                            #)
        
        #book = Book.objects.all().filter(id=request.data["id"]).values()

        #return Response({'Messages':'new book added','Book':book})
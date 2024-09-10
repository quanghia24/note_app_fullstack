from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, NoteSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Note



# Django generic views are just view functions (regular old python functions) that do things that are very common in web applications.
# Depending on the type of app you are building, they can save you from writing a lot of very simple views.

# Create your views here.
class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class NoteListCreate(generics.ListCreateAPIView): # list or and create new node
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated] # only one with correct jwt key can read

    def get_queryset(self):
        user = self.request.user # get the user currently interacting with this route
        return Note.objects.filter(author = user)

    def perform_create(self, serializer):
        if(serializer.is_valid()):
            serializer.save(author=self.request.user)
        else:
            print(serializer.errors)
    
class NoteDelete(generics.DestroyAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author = user)
    
    
    




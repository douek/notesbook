from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Note, UserProfile
from django.contrib.auth.models import User
from .serializers import NoteSerializer, ProfileSerializer
# Create your views here.


def user_profile(request, profile_id):
    """
    User Profile
    """
    try:
        userProfile = UserProfile.objects.get(pk=profile_id)
    except UserProfile.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ProfileSerializer(userProfile)
        return JsonResponse(serializer.data)

def user_notes(request, user_id):
    """
    List all code notes, or create a new note.
    """
    if request.method == 'GET':
        notes = Note.objects.filter(user = user_id)
        serializer = NoteSerializer(notes, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = NoteSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

def notes_list(request):
    """
    List all code notes, or create a new note.
    """
    if request.method == 'GET':
        notes = Note.objects.all()
        serializer = NoteSerializer(notes, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = NoteSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

def note_detail(request,note_id):
    """
    Retrieve, update or delete a note
    """
    try:
        note = Note.objects.get(pk=note_id)
    except Note.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == 'GET':
        serializer = NoteSerializer(note)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = NoteSerializer(note, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        note.delete()
        return HttpResponse(status=204)
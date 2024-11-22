# ringtones_app/views.py
from django.http import Http404
from ninja import NinjaAPI, Schema
from ninja.pagination import paginate
from django.shortcuts import get_object_or_404
from .models import Ringtone
from typing import List
from django.db.models import Q

api = NinjaAPI()


class RingtoneSchema(Schema):
    id: int
    name: str
    letter: str
    gender: int
    ringtone_url: str


# API Endpoints
@api.get("/letters/", response=List[str])
def get_letters(request, gender: int = None):
    if gender is not None and gender not in [0, 1]:
        raise Http404("Invalid gender format")
    if gender is not None:
        letters = Ringtone.objects.filter(gender=gender).values_list('letter', flat=True).distinct()
    else:
        letters = Ringtone.objects.values_list('letter', flat=True).distinct()
    return sorted(set(letters))


@api.get("/names/{letter}", response=List[RingtoneSchema])
@paginate
def get_names(request, letter: str, gender: int = None):
    if gender is not None and gender not in [0, 1]:
        raise Http404("Invalid gender format")
    if len(letter) != 1:
        raise Http404("Invalid letter format")
    if gender is not None:
        ringtones = Ringtone.objects.filter(gender=gender, letter__iexact=letter)
    else:
        ringtones = Ringtone.objects.filter(letter__iexact=letter)
    return [
        RingtoneSchema(
            id=ringtone.id,
            name=ringtone.name,
            letter=ringtone.letter,
            gender=ringtone.gender,
            ringtone_url=request.build_absolute_uri(ringtone.ringtone_file.url)
        ) for ringtone in ringtones
    ]


@api.get("/ringtone/{id}", response=RingtoneSchema)
def get_ringtone(request, id: int):
    ringtone = get_object_or_404(Ringtone, id=id)
    file_url = ringtone.ringtone_file.url
    return RingtoneSchema(id=ringtone.id, name=ringtone.name, letter=ringtone.letter, gender=ringtone.gender, ringtone_url=request.build_absolute_uri(file_url))


@api.get("/search/", response=List[RingtoneSchema])
@paginate
def search_ringtones(request, query: str, gender: int = None):
    if gender is not None and gender not in [0, 1]:
        raise Http404("Invalid gender format")
    if gender is not None:
        ringtones = Ringtone.objects.filter(gender=gender).filter(Q(name__icontains=query) | Q(letter__iexact=query))
    else:
        ringtones = Ringtone.objects.filter(Q(name__icontains=query) | Q(letter__iexact=query))
    return [
        RingtoneSchema(
            id=ringtone.id,
            name=ringtone.name,
            letter=ringtone.letter,
            gender=ringtone.gender,
            ringtone_url=request.build_absolute_uri(ringtone.ringtone_file.url)
        ) for ringtone in ringtones
    ]
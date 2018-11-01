from django.shortcuts import render
import os
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from json import JSONEncoder

# Create your views here.


@csrf_exempt
def test (request):
    print(request.POST['contact'])
    contact_name = request.POST['contact']
    os.system('notify-send -t 10000 -u critical '+"'phone ringing '" + '"'+contact_name+'"')
    return JsonResponse({'result':'ok'},
    encoder=JSONEncoder)

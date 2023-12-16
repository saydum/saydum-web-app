from django.shortcuts import render

from django.http import HttpResponse
from git import Repo
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def webhook(request):
    if request.method == 'POST':
        repo = Repo('./saydum-web-app')
        git = repo.git
        git.checkout('master')
        git.pull()
        return HttpResponse('pulled_success')
    return HttpResponse('get_request', status=400)
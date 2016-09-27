from django.shortcuts import render_to_response
from django.contrib.auth.models import User

def home(request):
    return render_to_response('tes/index.html', {'user': User})
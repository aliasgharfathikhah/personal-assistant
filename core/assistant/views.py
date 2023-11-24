from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from utils import Alex

def home(request):
    return render(request, 'pages/index.html')

@csrf_exempt
def run_script(request):
    p = Alex.run()
    return HttpResponse(p)

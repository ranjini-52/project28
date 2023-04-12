from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def form(request):





    return render(request,'form.html')
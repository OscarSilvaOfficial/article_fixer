from django.http import HttpResponse
from django.shortcuts import render

def home(request):
  if request.method == 'POST':
    description = request.POST.get('description')
    return HttpResponse(f"Description received: {description}")
  
  return render(request, 'index.html') 

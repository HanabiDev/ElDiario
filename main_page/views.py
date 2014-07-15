from django.shortcuts import render_to_response
from django.template import RequestContext
from models import *
from content.models import Category
# Create your views here.

def load_manager(request):

  categories = Category.objects.all();

  return render_to_response('manager.html', {'categories':categories}, context_instance=RequestContext(request))

def save_positions(request):

  for label in ['A','B','C','D','E','F','G','H','I','J']:
    position = Position.objects.get(label=label)
    category_id = request.POST.get(label)
    category = Category.objects.get(id=int(category_id))

    position.category = category
    position.save()

  return 

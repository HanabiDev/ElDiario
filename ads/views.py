from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from models import *
from forms import *
# Create your views here.

TEMPLATE_DIR = 'ads/../'

def home(request):
	ads = Ad.objects.all()
	return render_to_response(TEMPLATE_DIR+'ads_index.html', {'ads':ads}, 
		context_instance=RequestContext(request))

def add_ad(request):
	if request.method == 'GET':
		form = AdForm()
		return render_to_response(TEMPLATE_DIR+'add_edit_ad.html', {'form':form}, 
			context_instance=RequestContext(request))

	if request.method == 'POST':

		form = AdForm(request.POST, request.FILES)

		if form.is_valid():
			form.save()

			return redirect('/backend/publicidad')

		return render_to_response(TEMPLATE_DIR+'add_edit_ad.html', {'form':form},
			context_instance=RequestContext(request))

def edit_ad(request, id):

	ad = Ad.objects.get(id=id)

	if request.method == 'GET':
		form = AdForm(instance=ad)
		return render_to_response(TEMPLATE_DIR+'add_edit_ad.html', {'form':form, 'editing':True, 'title':ad.title}, 
			context_instance=RequestContext(request))

	if request.method == 'POST':

		form = AdForm(request.POST, request.FILES, instance=ad)

		if form.is_valid():

			form.save()

			return redirect('/backend/publicidad')

		return render_to_response(TEMPLATE_DIR+'add_edit_ad.html', {'form':form, 'editing':True, 'title':ad.title},
			context_instance=RequestContext(request))

def publish_group(request):
	ids = request.POST.getlist('id')

	for id in ids:
		ad = Ad.objects.get(id=id)
		ad.published = True
		ad.save()

	return redirect('/backend/publicidad')

def unpublish_group(request):
	ids = request.POST.getlist('id')

	for id in ids:
		ad = Ad.objects.get(id=id)
		ad.published = False
		ad.save()

	return redirect('/backend/publicidad')



def toggle_publish(request, id):
	ad = Ad.objects.get(id=id)
	ad.published = not ad.published
	ad.save()

	return redirect('/backend/publicidad')

def delete_ad(request):

	ids = request.POST.getlist('id')

	for id in ids:
		ad = Ad.objects.get(id=id)
		ad.delete()

	return redirect('/backend/publicidad')




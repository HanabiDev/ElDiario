from django.shortcuts import render_to_response, HttpResponseRedirect, redirect
from django.template import RequestContext
from content.models import Category
from photogallery.models import Gallery
from models import *
from forms import *
from django.contrib.auth.decorators import permission_required, login_required


TEMPLATE_DIR = 'vive_boyaca/../'

@login_required(login_url='login')
def list_towns(request):

	towns = Town.objects.all()

	return render_to_response(TEMPLATE_DIR+'towns/index.html', {'towns':towns},
							   context_instance=RequestContext(request))

@login_required(login_url='login')
@permission_required('vive_boyaca.add_town', login_url='/backend/permisos_insuficientes/')
def add_town(request):

	if request.method == 'GET':
		form = TownForm()
		return render_to_response(TEMPLATE_DIR+'towns/add_edit_town.html', {'form':form}, context_instance=RequestContext(request))

	if request.method == 'POST':
		form = TownForm(request.POST, request.FILES)

		if form.is_valid():
			
			new_town = form.save()

			try:
				town_category = Category.objects.create(
					title = new_town.name,
					description = 'Noticias del municipio de ' + new_town.name,
					parent = Category.objects.get(slug='vive-boyaca'),
					author=request.user
				)
			except Exception, e:
				pass

			return redirect('/backend/vive_boyaca/')

		return render_to_response(TEMPLATE_DIR+'towns/add_edit_town.html', {'form':form}, context_instance=RequestContext(request))


@login_required(login_url='login')
@permission_required('vive_boyaca.change_town', login_url='/backend/permisos_insuficientes/')
def edit_town(request, id):

	town = Town.objects.get(id=id)
	if request.method == 'GET':
		form = TownForm(instance=town)
		return render_to_response(TEMPLATE_DIR+'towns/add_edit_town.html', {'form':form, 'editing':True, 'title':town.name}, context_instance=RequestContext(request))

	if request.method == 'POST':
		form = TownForm(request.POST, request.FILES, instance=town)

		if form.is_valid():
			new_town = form.save()

			try:
				town_category = Category.objects.create(
					title = new_town.name,
					description = 'Noticias del municipio de ' + new_town.name,
					parent = Category.objects.get(slug='vive-boyaca'),
					author=request.user
				)
			except Exception, e:
				pass

			return redirect('/backend/vive_boyaca/')

		return render_to_response(TEMPLATE_DIR+'towns/add_edit_town.html', {'form':form, 'editing':True, 'title':town.name}, context_instance=RequestContext(request))


@login_required(login_url='login')
@permission_required('vive_boyaca.change_town', login_url='/backend/permisos_insuficientes/')
def publish_group(request):
	ids = request.POST.getlist('id')
	for town_id in ids:
		town = Town.objects.get(id=int(town_id))
		town.published = True
		town.save()
	return HttpResponseRedirect('/backend/vive_boyaca')

@login_required(login_url='login')
@permission_required('vive_boyaca.change_town', login_url='/backend/permisos_insuficientes/')
def unpublish_group(request):
	ids = request.POST.getlist('id')
	for town_id in ids:
		town = Town.objects.get(id=int(town_id))
		town.published = False
		town.save()
	return HttpResponseRedirect('/backend/vive_boyaca')

@login_required(login_url='login')
@permission_required('vive_boyaca.change_town', login_url='/backend/permisos_insuficientes/')
def toggle_publish(request, id):
	town = Town.objects.get(id=id)
	town.published = not town.published
	town.save()
	return HttpResponseRedirect('/backend/vive_boyaca')


@login_required(login_url='login')
@permission_required('vive_boyaca.delete_town', login_url='/backend/permisos_insuficientes/')
def delete_town(request):
	ids = request.POST.getlist('id')

	for id in ids:
		town = Town.objects.get(id=id)
		town.delete()

	return HttpResponseRedirect('/backend/vive_boyaca')

@login_required(login_url='login')
def poi_home(request):

	pois = PointOfInterest.objects.all()

	return render_to_response(TEMPLATE_DIR+'poi/index.html', {'pois':pois},
							   context_instance=RequestContext(request))

@login_required(login_url='login')
@permission_required('vive_boyaca.add_pointofinterest', login_url='/backend/permisos_insuficientes/')
def add_poi(request):

	if request.method == 'GET':
		form = POIForm()
		return render_to_response(TEMPLATE_DIR+'poi/add_edit_poi.html', {'form':form}, context_instance=RequestContext(request))

	if request.method == 'POST':
		form = POIForm(request.POST)

		if form.is_valid():
			
			new_poi = form.save()

			return redirect('/backend/vive_boyaca/poi/')

		return render_to_response(TEMPLATE_DIR+'poi/add_edit_poi.html', {'form':form}, context_instance=RequestContext(request))

@login_required(login_url='login')
@permission_required('vive_boyaca.change_pointofinteres', login_url='/backend/permisos_insuficientes/')
def edit_poi(request, id):

	poi = PointOfInterest.objects.get(id=id)
	if request.method == 'GET':
		form = POIForm(instance=poi)
		return render_to_response(TEMPLATE_DIR+'poi/add_edit_poi.html', {'form':form, 'editing':True, 'title':poi.name}, context_instance=RequestContext(request))

	if request.method == 'POST':
		form = POIForm(request.POST, instance=poi)

		if form.is_valid():
			new_poi = form.save()

			return redirect('/backend/vive_boyaca/poi/')

		return render_to_response(TEMPLATE_DIR+'poi/add_edit_poi.html', {'form':form, 'editing':True, 'title':poi.name}, context_instance=RequestContext(request))


@login_required(login_url='login')
@permission_required('vive_boyaca.delete_pointofinterest', login_url='/backend/permisos_insuficientes/')
def delete_poi(request):
	ids = request.POST.getlist('id')

	for id in ids:
		poi = PointOfInterest.objects.get(id=id)
		poi.delete()

	return HttpResponseRedirect('/backend/vive_boyaca/poi/')

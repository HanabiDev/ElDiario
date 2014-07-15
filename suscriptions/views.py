# Create your views here.
#encoding: utf-8
from django.shortcuts import render_to_response, HttpResponseRedirect, redirect
from django.template import RequestContext
from models import *
from forms import *
from django.contrib.auth.decorators import permission_required, login_required
from content.models import Category
# Create your views here.

TEMPLATE_DIR = 'suscriptions/../'

@login_required(login_url='login')
def list_suscriptions(request):
	suscriptions = Suscription.objects.all()

	return render_to_response(TEMPLATE_DIR+'susc_index.html', {'suscribed_list':suscriptions},
							   context_instance=RequestContext(request))


@login_required(login_url='login')
@permission_required('suscriptions.add_suscription', login_url='/backend/permisos_insuficientes/')
def add_suscription(request):

	if request.method == 'GET':
		form = SuscriptionForm()
		return render_to_response(TEMPLATE_DIR+'add_edit_susc.html',
							  {'form':form}, context_instance=RequestContext(request))

	elif request.method == 'POST':
		form = SuscriptionForm(request.POST)
        if form.is_valid():
            new_suscription = form.save()
            return HttpResponseRedirect('/backend/suscripciones')
        else:
        	return render_to_response(TEMPLATE_DIR+'add_edit_susc.html',
							  {'form':form}, context_instance=RequestContext(request))

@login_required(login_url='login')
@permission_required('suscriptions.edit_suscription', login_url='/backend/permisos_insuficientes/')
def edit_suscription(request, id):

	suscription = Suscription.objects.get(id=id)
	full_name = suscription.first_name+' '+suscription.last_name
	if request.method == 'GET':
		form = SuscriptionForm(instance=suscription)
		return render_to_response(TEMPLATE_DIR+'add_edit_susc.html',
							  {'form':form, 'editing': True, 'title': full_name}, context_instance=RequestContext(request))

	elif request.method == 'POST':
		form = SuscriptionForm(request.POST, instance=suscription)
        if form.is_valid():
            new_suscription = form.save()
            return HttpResponseRedirect('/backend/suscripciones')
        else:
        	return render_to_response(TEMPLATE_DIR+'add_edit_susc.html',
							  {'form':form, 'editing': True, 'title': full_name}, context_instance=RequestContext(request))

@login_required(login_url='login')
@permission_required('suscriptions.edit_suscription', login_url='/backend/permisos_insuficientes/')
def activate_group(request):

	ids = request.POST.getlist('id')

	for id in ids:
		suscription = Suscription.objects.get(id=id)
		suscription.status = True
		suscription.save()

	return HttpResponseRedirect('/backend/suscripciones')

@login_required(login_url='login')
@permission_required('suscriptions.edit_suscription', login_url='/backend/permisos_insuficientes/')
def deactivate_group(request):

	ids = request.POST.getlist('id')

	for id in ids:
		suscription = Suscription.objects.get(id=id)
		suscription.status = False
		suscription.save()

	return HttpResponseRedirect('/backend/suscripciones')

@login_required(login_url='login')
@permission_required('suscriptions.edit_suscription', login_url='/backend/permisos_insuficientes/')
def toggle_publish(request, id):

	suscription = Suscription.objects.get(id=id)
	suscription.status = not suscription.status
	suscription.save()
	return HttpResponseRedirect('/backend/suscripciones')


@login_required(login_url='login')
@permission_required('suscriptions.delete_suscription', login_url='/backend/permisos_insuficientes/')
def delete_suscription(request):

	ids = request.POST.getlist('id')

	for id in ids:
		suscription = Suscription.objects.get(id=id)
		suscription.delete()

	return HttpResponseRedirect('/backend/suscripciones')

def frontend_suscription(request):

	if request.method == 'GET':
		form = SuscriptionForm()
		categories = Category.objects.filter(parent=None)
		return render_to_response('frontend/../add_susc.html',
								{'form':form, 'categories': categories}, context_instance=RequestContext(request))

	elif request.method == 'POST':
		form = SuscriptionForm(request.POST)
		if form.is_valid():
			new_suscription = form.save()
			return render_to_response('frontend/../add_susc.html',
									{'done':True}, context_instance=RequestContext(request))
		else:
			return render_to_response('frontend/../add_susc.html',
			{'form':form}, context_instance=RequestContext(request))

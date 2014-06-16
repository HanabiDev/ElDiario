#encoding: utf-8
from django.shortcuts import render_to_response, redirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

TEMPLATE_DIR = 'admin/../'

def admin_login(request):

	if request.user.is_authenticated():
		print request.user

		return redirect('/backend')

	if request.method == 'GET':
		form = AuthenticationForm(request)

		return render_to_response(
			TEMPLATE_DIR+'login.html', 
			{'form':form},
      		context_instance=RequestContext(request)
	    )

	elif request.method == 'POST':

		form = AuthenticationForm(request.POST)

		username = request.POST.get('username')
		password = request.POST.get('password')

		form.fields['username'].initial = username

		if not username:	
			form_err = {'username_errors':'Ingresa un nombre de usuario'}
			return render_to_response(
				TEMPLATE_DIR+'login.html', 
				{'form':form, 'form_err':form_err},
				context_instance=RequestContext(request)
			)	
		if not password:
			form_err = {'password_errors':'Ingresa una contraseña'}
			return render_to_response(
				TEMPLATE_DIR+'login.html', 
				{'form':form, 'form_err':form_err},
				context_instance=RequestContext(request)
			)	

		user = authenticate(username=username, password=password)

		if user is not None:
			if user.is_active:
				login(request, user)
				return redirect('/backend')
			else:
				form_err = {}
				form_err['error'] = 'Esta cuenta está deshabilitada'
				
				return render_to_response(
					TEMPLATE_DIR+'login.html', 
					{'form':form, 'form_err':form_err},
					context_instance=RequestContext(request)
				)
		else:
			form_err = {}
			form_err['error'] = 'Esta cuenta no existe o la contraseña no coincide'
			return render_to_response(
				TEMPLATE_DIR+'login.html', 
				{'form':form, 'form_err':form_err},
				context_instance=RequestContext(request)
			)

def admin_logout(request):
	if not request.user.is_authenticated():
		return redirect('login')

	logout(request)
	return render_to_response(TEMPLATE_DIR+'logout.html')

@login_required(login_url='login')
def set_new_password(request):
	if request.method == 'GET':
		form = PasswordChangeForm(request.user, None)
		return render_to_response(
			TEMPLATE_DIR+'set_password.html', 
			{'form':form},
			context_instance=RequestContext(request)
		)
	elif request.method == 'POST':

		form = PasswordChangeForm(request.user, request.POST)

		if form.is_valid():
			form.save()
			return redirect('/backend/')
		else:
			return render_to_response(
				TEMPLATE_DIR+'set_password.html', 
				{'form':form},
				context_instance=RequestContext(request)
			)	

def no_perms(request):
	return render_to_response(TEMPLATE_DIR+'permission_err.html')

@login_required(login_url='login')
def home(request):
	return render_to_response(TEMPLATE_DIR+'index.html', request.session, 
							  context_instance=RequestContext(request))


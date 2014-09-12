from django.shortcuts import render_to_response, redirect
from django.contrib.auth.models import User, Group
from forms import *
from django.template import RequestContext

from django.contrib.auth.decorators import permission_required, login_required


TEMPLATE_DIR = 'auth/../'


@login_required(login_url='login')
def home(request):

	users = User.objects.all()
	groups = Group.objects.all()
	for group in groups:
		group.members = group.user_set.all().count()

	return render_to_response(TEMPLATE_DIR+'auth_index.html', {'users':users, 'groups':groups}, 
								 context_instance=RequestContext(request))

"""
-------------------------------------------------------------------------------------
User views
-------------------------------------------------------------------------------------
"""

@login_required(login_url='login')
@permission_required('auth.add_user', login_url='/backend/permisos_insuficientes/')
def add_user(request):

	if request.method == 'GET':
		form = UserAddForm()
		return render_to_response(TEMPLATE_DIR+'add_edit.html', {'form':form}, context_instance=RequestContext(request))
	
	elif request.method == 'POST':
		form = UserAddForm(request.POST)
        if form.is_valid():
            new_user = form.save()

            return redirect('/backend/acceso/usuarios/editar/'+str(new_user.id))
        else:
        	return render_to_response(TEMPLATE_DIR+'add_edit.html',
							  {'form':form}, context_instance=RequestContext(request))



@login_required(login_url='login')
@permission_required('auth.change_user', login_url='/backend/permisos_insuficientes/')
def edit_user(request, id):

	if request.method == 'GET':
		user = User.objects.get(id=id)
		form = UserEditForm(instance=user)
		return render_to_response(TEMPLATE_DIR+'add_edit.html', {'form':form, 'editing':True, 'username':user.username}, 
						context_instance=RequestContext(request))

	elif request.method == 'POST':
		user = User.objects.get(id=id)
		form = UserEditForm(request.POST, instance=user)
		if form.is_valid():
			new_user = form.save()

			if request.FILES:
				new_user.avatar = request.FILES['avatar']
				new_user.save()
			
			return redirect('/backend/acceso/')

        else:
        	return render_to_response(TEMPLATE_DIR+'add_edit.html',
							  {'form':form}, context_instance=RequestContext(request))


@login_required(login_url='login')
@permission_required('auth.change_user', login_url='/backend/permisos_insuficientes/')
def change_pass(request, id):

	if request.method == 'GET':
		user = User.objects.get(id=id)
		form = ChangePassForm()
		return render_to_response(TEMPLATE_DIR+'add_edit.html', {'form':form, 'editing':True,'editing_pass':True, 'username':user.username}, 
						context_instance=RequestContext(request))

	elif request.method == 'POST':
		user = User.objects.get(id=id)
		form = ChangePassForm(request.POST)

        if form.is_valid():
        	form.user = user
        	new_pass = form.save()
        	return redirect('/backend/acceso/usuarios/editar/'+str(id))
        else:
        	#raise Exception('Hola')
        	return render_to_response(TEMPLATE_DIR+'add_edit.html',
							  {'form':form, 'editing':True, 'editing_pass':True, 'username':user.username}, 
							  context_instance=RequestContext(request))


@login_required(login_url='login')
@permission_required('auth.change_user', login_url='/backend/permisos_insuficientes/')
def toggle_lock_group(request):
	ids = request.POST.getlist('id')

	for id in ids:
		user = User.objects.get(id=id)
		user.is_active = False
		user.save()

	return redirect('/backend/acceso')


@login_required(login_url='login')
@permission_required('auth.change_user', login_url='/backend/permisos_insuficientes/')
def toggle_unlock_group(request):
	ids = request.POST.getlist('id')

	for id in ids:
		user = User.objects.get(id=id)
		user.is_active = True
		user.save()

	return redirect('/backend/acceso')


@login_required(login_url='login')
@permission_required('auth.change_user', login_url='/backend/permisos_insuficientes/')
def toggle_lock(request, id):
	user = User.objects.get(id=id)
	user.is_active = not user.is_active
	user.save()

	return redirect('/backend/acceso')


"""
-------------------------------------------------------------------------------------
Group views
-------------------------------------------------------------------------------------
"""
@login_required(login_url='login')
@permission_required('auth.add_group', login_url='/backend/permisos_insuficientes/')
def add_group(request):

	if request.method == 'GET':
		form = GroupAddForm()
		return render_to_response(TEMPLATE_DIR+'add_edit_group.html', {'form':form}, context_instance=RequestContext(request))
	
	elif request.method == 'POST':
		form = GroupAddForm(request.POST)
        if form.is_valid():
            new_group = form.save()
            return redirect('/backend/acceso/grupos')

        else:
        	return render_to_response(TEMPLATE_DIR+'add_edit_group.html',
							  {'form':form}, context_instance=RequestContext(request))


@login_required(login_url='login')
@permission_required('auth.change_group', login_url='/backend/permisos_insuficientes/')
def edit_group(request, id):

	if request.method == 'GET':
		group = Group.objects.get(id=id)
		form = GroupAddForm(instance=group)
		return render_to_response(TEMPLATE_DIR+'add_edit.html', {'form':form, 'editing':True, 'groupname':group.name}, 
						context_instance=RequestContext(request))

	elif request.method == 'POST':
		group = Group.objects.get(id=id)
		form = GroupAddForm(request.POST, instance=group)
        if form.is_valid():
            new_group = form.save()
            return redirect('/backend/acceso/')
        else:
        	return render_to_response(TEMPLATE_DIR+'add_edit_group.html',
							  {'form':form}, context_instance=RequestContext(request))


def delete_group(request):

	ids = request.POST.getlist('group_id')

	for id in ids:
		group = Group.objects.get(id=id)
		group.delete()

	return redirect('/backend/acceso')





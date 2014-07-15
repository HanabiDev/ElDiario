#encoding: utf-8
from django.shortcuts import render_to_response, HttpResponseRedirect
from django.template import RequestContext
from models import *
from forms import *
# Create your views here.

TEMPLATE_DIR = 'photogallery/../'

def home(request):
	galleries = Gallery.objects.all()
	for gallery in galleries:
		images = gallery.images.all().count()
		gallery.images_count = images

	return render_to_response(TEMPLATE_DIR+'index_gallery.html', {'galleries':galleries},
								context_instance=RequestContext(request))

def add_gallery(request):

	if request.method == 'GET':
		form = GalleryForm()
		image_form = ImageForm()
		available_images = Image.objects.all()

		return render_to_response(TEMPLATE_DIR+'add_edit_gallery.html',
							  {'form':form, 'image_form':image_form, 'available_images':available_images},
							  context_instance=RequestContext(request))

	elif request.method == 'POST':
		form = GalleryForm(request.POST)
		if form.is_valid():
			new_galery = form.save()
			return HttpResponseRedirect('/backend/fotogalerias/editar/'+str(new_galery.id))
		else:
			return render_to_response(TEMPLATE_DIR+'add_edit_gallery.html',
					  {'form':form}, context_instance=RequestContext(request))

def edit_gallery(request, id):

	gallery = Gallery.objects.get(id=id)

	if request.method == 'GET':
		image_form = ImageForm()
		form = GalleryForm(instance=gallery)
		gallery_images = gallery.images.all()
		available_images = Image.objects.exclude(id__in=gallery_images.values_list('id'))


		for img in available_images:
			print img

		return render_to_response(TEMPLATE_DIR+'add_edit_gallery.html',
							  {'form':form, 'editing':True, 'title':gallery.title,
							   'image_form': image_form, 'g_images':gallery_images,
							   'available_images': available_images},
							  context_instance=RequestContext(request))

	elif request.method == 'POST':
		form = GalleryForm(request.POST, instance=gallery)
        if form.is_valid():
            new_gallery = form.save()
            return HttpResponseRedirect('/backend/fotogalerias')
        else:
        	return render_to_response(TEMPLATE_DIR+'add_edit_gallery.html',
							  {'form':form, 'editing':True, 'title':gallery.title}, context_instance=RequestContext(request))

def publish_group(request):
	ids = request.POST.getlist('id')
	for gallery_id in ids:
		gallery = Gallery.objects.get(id=int(gallery_id))
		gallery.published = True
		gallery.save()
	return HttpResponseRedirect('/backend/fotogalerias')

def unpublish_group(request):
	ids = request.POST.getlist('id')
	for gallery_id in ids:
		gallery = Gallery.objects.get(id=int(gallery_id))
		gallery.published = False
		gallery.save()
	return HttpResponseRedirect('/backend/fotogalerias')

def toggle_publish(request, id):
	gallery = Gallery.objects.get(id=id)
	gallery.published = not gallery.published
	gallery.save()
	return HttpResponseRedirect('/backend/fotogalerias')

def delete_gallery(request):
	ids = request.POST.getlist('id')
	for gallery_id in ids:
		gallery = Gallery.objects.get(id=int(gallery_id))
		gallery.delete()
	return HttpResponseRedirect('/backend/fotogalerias')



import json
from django.http import HttpResponse



def upload(request):
	response_data = {}

	if request.method == 'GET':
		form = ImageForm()
		return render_to_response(TEMPLATE_DIR+'upload_test.html',
							  {'form':form}, context_instance=RequestContext(request))

	if request.method=='POST':    #.is_ajax():

		form = ImageForm(request.POST, request.FILES)

		print request.POST
		print request.FILES

		if form.is_valid():

			upload = Image(
				image=request.FILES['image']
			)

			upload.image_title = request.POST.get('image_title')
			upload.author = request.POST.get('author')
			upload.description = request.POST.get('description')

			upload.save()

			response_data['status'] = "success"
			response_data['fileLink'] = "/%s" % upload.image
			response_data['id'] = upload.id
			response_data['author'] = upload.author
			response_data['title'] = upload.image_title

			return HttpResponse(json.dumps(response_data), content_type="application/json")
		else:
			return HttpResponse("error")


	response_data['status'] = "error"
	response_data['result'] = "We're sorry, but something went wrong. Please be sure that your file respects the upload conditions."

	return HttpResponse(json.dumps(response_data), content_type='application/json')

from django.shortcuts import render_to_response, HttpResponseRedirect, redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

TEMPLATE_DIR = 'conf/../'
# Create your views here.

@login_required(login_url='login')
def home(request):
	if request.method == 'GET':
		settings = load_settings()
		print settings
		return render_to_response(
			TEMPLATE_DIR+'settings.html', 
			{'settings':settings}, 
			context_instance=RequestContext(request)
		)

	if request.method == 'POST':
		data = {}

		for setting in request.POST:
			if not setting == 'csrfmiddlewaretoken':
				data[setting] = request.POST.get(setting)

		save_settings(data)
		
		return HttpResponseRedirect('/backend')



import io, json, os.path
def save_settings(data):
	filepath = os.path.dirname(__file__)
	with io.open(filepath+'/conf.json', 'w', encoding='utf-8') as f:
	  f.write(unicode(json.dumps(data, ensure_ascii=False)))
	  f.close()

def load_settings():
	filepath = os.path.dirname(__file__)
	with io.open(filepath+'/conf.json', 'r', encoding='utf-8') as f:
		content = f.read()
		dumped_data = json.loads(content)
		
		data = []
		for setting in dumped_data:
			data.append((setting, dumped_data[setting]))

	return data
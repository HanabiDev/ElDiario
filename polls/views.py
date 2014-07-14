from django.shortcuts import render_to_response, HttpResponse, redirect, get_object_or_404
from django.template import RequestContext
from models import Poll, Option
from forms import PollForm

# Create your views here.

def list_polls(request):
	polls = Poll.objects.all()
	for poll in polls:
		votes = 0
		for option in poll.option_set.all():
			votes += option.hits
		poll.votes = votes

	return render_to_response('polls_index.html', {'polls':polls}, context_instance=RequestContext(request))

def add_poll(request):
	if request.method == 'GET':
		form = PollForm()
		return render_to_response('add_edit_poll.html', {'form':form}, context_instance=RequestContext(request))

	if request.method == 'POST':
		form = PollForm(request.POST)
		if form.is_valid():
			Poll.objects.all().update(closed=True)
			poll = form.save()

			return redirect('/backend/encuestas/editar/'+str(poll.id))

		return render_to_response('add_edit_poll.html', {'form':form}, context_instance=RequestContext(request))

def edit_poll(request, id):

	poll = Poll.objects.get(id=id)

	options = options = poll.option_set.all()

	if request.method == 'GET':
		form = PollForm(instance=poll)
		return render_to_response('add_edit_poll.html',
			{'form':form, 'options':options,'editing':True, 'title':poll.poll_title},
			context_instance=RequestContext(request))

	if request.method == 'POST':
		form = PollForm(request.POST, instance=poll)
		if form.is_valid():
			poll = form.save()

			poll.option_set.all().delete()

			options = request.POST.getlist('options')
			for option in options:
				if option:
					new_opt = Option.objects.create(poll=poll, question_text= option)
					new_opt.save()

			return redirect('/backend/encuestas')

		return render_to_response('add_edit_poll.html',
			{'form':form, 'editing':True, 'title':poll.poll_title},
			context_instance=RequestContext(request))

def toggle_publish(request, id):
	Poll.objects.exclude(id=id).update(closed=True)
	poll = Poll.objects.get(id=id)
	poll.closed = not poll.closed
	try:
		del request.session['voted']
	except Exception as e:
		pass
	poll.save()
	return redirect('/backend/encuestas')

def delete_poll(request):
	ids = request.POST.getlist('id')
	for id in ids:
		poll = Poll.objects.get(id=int(id))
		poll.delete()

	return redirect('/backend/encuestas')

def vote(request):
	id = request.POST.get('vote')
	option = Option.objects.get(id=id)
	option.hits = option.hits + 1
	option.save()

	request.session['voted']=True

	poll = option.poll

	return get_results(request, poll.id)


def get_results(request, id):

	poll = Poll.objects.get(id=id)

	votes = 0
	for opt in poll.option_set.all():
		votes += opt.hits
	poll.votes = votes

	print request.session['voted']

	return render_to_response('poll_results.html', {'poll':poll})

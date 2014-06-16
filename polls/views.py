from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from models import Poll
from forms import PollForm

# Create your views here.

def list_polls(request):
	polls = Poll.objects.all()
	for poll in polls:
		poll.votes = poll.vote_set.all().count()

	return render_to_response('polls_index.html', {'polls':polls})

def add_poll(request):
	if request.method == 'GET':
		form = PollForm()
		return render_to_response('add_edit_poll.html', {'form':form}, context_instance=RequestContext(request))

	if request.method == 'POST':	
		form = PollForm(request.POST)
		if form.is_valid():
			form.save()

			return redirect('/backend/encuestas')

		return render_to_response('add_edit_poll.html', {'form':form}, context_instance=RequestContext(request))

def edit_poll(request, id):

	poll = Poll.objects.get(id=id)

	if request.method == 'GET':
		form = PollForm(instance=poll)
		return render_to_response('add_edit_poll.html', {'form':form, 'editing':True, 'title':poll.poll_title}, context_instance=RequestContext(request))

	if request.method == 'POST':	
		form = PollForm(request.POST, instance=poll)
		if form.is_valid():
			form.save()

			return redirect('/backend/encuestas')

		return render_to_response('add_edit_poll.html', {'form':form, 'editing':True, 'title':poll.poll_title}, context_instance=RequestContext(request))

from django.shortcuts import render_to_response, HttpResponseRedirect,render, HttpResponse
from django.core.context_processors import csrf
from poll.forms import PollForm
from poll.models import Poll
from poll.message import clear_message
from poll.message import get_twilio_msg
from poll.message import kill_thread
from django.template import RequestContext, Context

# Create your views here.
def poll(request):
    open('/app/static/data.json', 'w').close()
    form = PollForm()
    try:
        clear_message()
    except Exception as ex:
        template = "An exception of type {0} occured. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        print message

    try:
        if request.POST:
            form = PollForm(request.POST)
            if form.is_valid():
                form.save()
                get_twilio_msg()
                return HttpResponseRedirect('/display/')
            else:
                print "form invalid"
        else:
            form = PollForm()

        args = {}
        args.update(csrf(request))
        args['form'] = form
        return render(request, 'home.html', args)

    except Exception as ex:
        template = "An exception of type {0} occured. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        print message
        args = {}
        args.update(csrf(request))
        args['form'] = form
        return render(request,'home.html')


def display(request):
    try:
        poll_data = Poll.objects.order_by('-pk')[0]
        return render(request, 'display.html', {'poll_data': poll_data})
    except:
        return render(request, 'display.html', {'poll_data': 'No Data Available'})


def get_hostname(request):
    print "Workin Sarvesh"
    kill_thread()
    return HttpResponseRedirect('/display/')

def disclosure(request):
    return render_to_response('disclosure.html')

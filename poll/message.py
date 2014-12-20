__author__ = 'srv'
from twilio.rest import TwilioRestClient
import json
from pollapp import settings
print settings.PROJECT_PATH
from poll.models import Poll
import threading

#Twilio Account and Toked Ids
account = ""
token = ""

client = TwilioRestClient(account, token)

t= None
def clear_message():
    for message in client.messages.list(to=): # to is set to a Twilio phone number on which you would receive sms. Eg:+19992223333
        message.delete_instance()


def get_poll_data():
    #print 'Get Poll Working'
    poll_data = Poll.objects.order_by('-pk')[0]
    poll_title = poll_data.Poll_Title
    poll_opt1 = poll_data.Option1
    poll_opt2 = poll_data.Option2
    poll_opt3 = poll_data.Option3
    poll_opt4 = poll_data.Option4
    poll_opt5 = poll_data.Option5
    return poll_title, poll_opt1, poll_opt2, poll_opt3, poll_opt4, poll_opt5


def get_twilio_msg():
    global t
    json_array = []
    poll_title, poll_opt1, poll_opt2, poll_opt3, poll_opt4, poll_opt5 = get_poll_data()

    if poll_opt1 != "":
        to_append = [str(poll_opt1), 0]
        json_array.append(to_append)
    if poll_opt2 != "":
        to_append = [str(poll_opt2), 0]
        json_array.append(to_append)
    if poll_opt3 != "":
        to_append = [str(poll_opt3), 0]
        json_array.append(to_append)
    if poll_opt4 != "":
        to_append = [str(poll_opt4), 0]
        json_array.append(to_append)
    if poll_opt5 != "":
        to_append = [str(poll_opt5), 0]
        json_array.append(to_append)

    for message in client.messages.list(to=+16508263017):
        for data in json_array:
            if message.body.lower() == data[0].lower():
                data[1] += 1
    json_data = json.dumps(json_array)
    with open('../PollApp/poll/static/data.json', 'w') as json_output:
        json_output.write(json_data)

    t = threading.Timer(5, get_twilio_msg)
    t.start()


def kill_thread():
    try:
        global t
        t.cancel()
        t.join()
        return
    except:
        return
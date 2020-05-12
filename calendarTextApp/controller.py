from gcsa.google_calendar import GoogleCalendar

from calendarTextApp import eventStringProducer

import datetime
import os
from calendarTextApp import model

from django.conf import settings

import requests


calendars = ['','']


def interpret(message, sender):

    kindText = message[:2]

    print(kindText[:1])

    if (kindText[:1] == "d" or kindText[:1] == 'D'):



        day = message[1:3]
        month = message[3:5]
        year = message[5:7]

        print("here2")

        niceDateString = day + '/' +month + '/' + year

        print(niceDateString)

        date = datetime.date(int('20' + year), int(month), int(day))


        thing = ['johnjoestack@gmail.com', '1j5rv7mttuajcbns9inh71pmak@group.calendar.google.com']





        eventString = eventStringProducer.individualDate(date, model.getEventsOneDate(date, thing), niceDateString)

        print(eventString)

        """
        if eventString.__len__() > 950:
            splitString = [eventString[i:i + n] for i in range(0, len(eventString), n)]

            for string in splitString:
                payload = {'username': 'johnjoestack@gmail.com',

                           'key': '8BEFF0B3-6095-D81C-7396-9F04BA9FA974',
                           'to': str(sender),
                           'message': string
                           }

                r = requests.post('https://api-mapper.clicksend.com/http/v2/send.php', params=payload)

        else:
            payload = {'username': 'johnjoestack@gmail.com',

                       'key': '8BEFF0B3-6095-D81C-7396-9F04BA9FA974',
                       'to': str(sender),
                       'message': eventString
                       }

            r = requests.post('https://api-mapper.clicksend.com/http/v2/send.php', params=payload)
        """





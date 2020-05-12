from gcsa.google_calendar import GoogleCalendar

import os


import operator


from calendarText.settings import STATIC_DIR
# after your other file variables

print("jeff" + STATIC_DIR)

creds = os.path.join(STATIC_DIR, 'credentials.json')






def getEventsOneDate(date, calendarChoice):



    print("in model")

    bigRawEventTuple = []

    bigRawAllDayEventTuple = []

    bigRawNotAllDayEventTuple = []

    print(calendarChoice)

    index = 0

    for name in calendarChoice:

        index += 1
        print(index)

        print(name
              )




        calendar = GoogleCalendar(name, creds)









        print(calendar)


        eventObjectArray = calendar.get_events(date, date, order_by='startTime')

        print(str(eventObjectArray))

        print(''
              'h')

        for event in eventObjectArray:

            print(str(event))



            rawEvent = []

            rawEvent.append(str(event.summary))
            rawEvent.append(str(event.location))

            print("in event")

            rawEvent.append(event.start.time())


            rawEvent.append(event.end.time())

            print(rawEvent)

            if len(str(event.start)) == 10:



                bigRawAllDayEventTuple.append(rawEvent)
                print("appending1")
            else:
                bigRawNotAllDayEventTuple.append(rawEvent)
                print("appending2")

    allDayEvents = sorted(bigRawAllDayEventTuple)

    notAllDayEvents = sorted(bigRawNotAllDayEventTuple, key=operator.itemgetter(1, 2))


    bigRawEventTuple = allDayEvents + notAllDayEvents




    return (allDayEvents, notAllDayEvents)
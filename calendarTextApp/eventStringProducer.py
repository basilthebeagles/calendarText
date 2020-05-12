from gcsa.google_calendar import GoogleCalendar
import datetime


def individualDate(date, eventArray, niceDateString):
    """

    :type eventArray: GoogleCalendar.get_events()
    :type date: datetime.date
    """







    eventString = "Events on " + date.strftime("%A %d %B %Y") + ':' + '\n' + '\n'

    for event in eventArray[0]:
        eventString += event[0] + '\n'

        if event.location != None:
            eventString += event[1] + '\n'

        eventString += ("All Day" + '\n' + '\n')

    for event in eventArray[1]:
        eventString += (event[0] + '\n')

        if event.location != None:
            eventString += event[1] + '\n'

        eventString += (str(event[2].isoformat(timespec='minutes')) + ' - ' + str(
            event[3].time().isoformat(timespec='minutes')) + '\n' + '\n')

    print(eventString)

    return eventString




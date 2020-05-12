from django.http import HttpResponse

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from calendarTextApp import controller


@csrf_exempt
def request(request):
    response = HttpResponse()
    rawPostData = request.GET

    try:
        print("here")
        print(rawPostData)

        print(request.GET)
        message = str(rawPostData.__getitem__('original_body'))
        sender = str(rawPostData.__getitem__('from'))

        controller.interpret(message, sender)




    except:
        response.status_code = 200

        return response


    response.status_code = 200
    return response

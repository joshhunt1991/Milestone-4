from django.http import HttpResponse


class StripeWH_Handler:
    # stripe webhook handler class

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        # handle generic events
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)

from django.http import HttpResponse
from twilio.rest import Client
from django.views.decorators.csrf import csrf_exempt

account_sid = 'AC63f3551ef42e0973953c04a91e75a53f'
auth_token = 'b8f9ffce10e6d6b51a54e024fc067b72'
client = Client(account_sid, auth_token)


@csrf_exempt
def bot(request):
    print(request.POST)
    message = request.POST["Body"]
    sender_name = request.POST["ProfileName"]
    sender_number = request.POST["From"]
    
    if message == "hi":
        client.messages.create(
        from_='whatsapp:+14155238886',
        body= f'Hi {sender_name}, your appointment is coming up on July 21 at 3PM',
        to= sender_number
        )
        
        print(message.sid)
    return HttpResponse("Hello")
from twilio.rest import Client

account_sid = 'AC0d79e56293d4494c36eee4f48a59ff8e'
auth_token = '15caae692cc9007c162f8d0c7f77e04d'

client = Client(account_sid, auth_token)

def send_message(message_, from_, to):
    print('whatsappFROM: ' + from_)
    print('whatsappTO: ' + to)

    if 'w' in list(to):
        message = client.messages \
            .create(
            body=message_,
            from_="whatsapp:"+ from_,
            to=to
        )
    else:
        message = client.messages \
            .create(
            body=message_,
            from_="whatsapp:" + from_,
            to="whatsapp:" + to
        )

    '''message = client.messages \
        .create(
        body=message_,
        from_="whatsapp:" + from_,
        to=to
    )'''

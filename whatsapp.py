import os
import twilio.rest import client

client=client()

from_whatsapp_number='whatsapp:+1 415 523 8886 '
to_whatsapp_number='whatsapp:'+os.environ['MY_WHATSAPP_NUMBER']


client.messages.create(body='Hello world',
                       from_=FROM_WHATSAPP_NUMBER,
                        to=TO_WHATSAPP_NUMBER)

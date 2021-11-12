import os
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = "ACb92722c0df15711ebc9c8a37f3609b64"
auth_token = "c06c3edd5b8c4ce730616e2b67915ec4"
client = Client(account_sid, auth_token)

message = client.messages.create(
    body='Hello there!',
    from_='whatsapp:+14155238886',
    to='whatsapp:+50686137588'
)

print(message.sid)

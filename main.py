from twilio.rest import Client

message = "Px8E3V0&*f3*7UD"


account_sid = "ACb92722c0df15711ebc9c8a37f3609b64"
auth_token = "c06c3edd5b8c4ce730616e2b67915ec4"


client = Client(account_sid, auth_token)

client.messages.create(
    to="+50686137588",
    from_="+12563048002",
    body=message
)

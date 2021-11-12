from twilio.rest import Client

message = "jejeje mejor no saquemos cuentas… Que bueno! Yo estoy de vuelta en La Suiza, después de muchos años de trabajar en San José, feliz de vivir acá de nuevo, por aquí todo es tan tranquilo y mucho más sano"


account_sid = "ACb92722c0df15711ebc9c8a37f3609b64"
auth_token = "c06c3edd5b8c4ce730616e2b67915ec4"


client = Client(account_sid, auth_token)

client.messages.create(
    to="+50686137588",
    from_="+12563048002",
    body=message
)

import os
from twilio.rest import Client
account_sid = ''
auth_token = ''
client = Client(account_sid, auth_token)


call = client.calls.create(
                        url='https://cdn.discordapp.com/attachments/928323556708872306/938646660177858610/venmo.xml',
                        to='+16197848029‬‬',
                        from_='+14789999928'
                    )

print(call.sid)
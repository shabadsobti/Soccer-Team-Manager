from twilio.rest import Client
from app import app

account_sid = app.config['ACCOUNT_SID']
auth_token  = app.config['AUTH_TOKEN']


client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+14344664943", 
    from_="+16109838407",
    body="Would you like to play tommorow?")

print(message.sid)
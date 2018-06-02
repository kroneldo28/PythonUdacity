from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC121feae79893a26b3644cb82bcf74734"
# Your Auth Token from twilio.com/console
auth_token  = "86614f1cb2a7d7f261476c0d1a6e813c"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+33612495192", 
    from_="+33757917179",
    body="Hello from Python! I sent this message using Twilio on Python")

print(message.sid)

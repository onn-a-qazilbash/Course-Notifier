from twilio.rest import Client

class TextMessage:
    def __init__(self, acct_sid, auth_tok, incoming, outgoing):

        self.client = Client(acct_sid, auth_tok)
        self.incoming = incoming
        self.outgoing = outgoing

        self.message = ""

    def add_message(self, message):
        self.message = message
        return None

    def send(self):
        self.client.messages.create(body=self.message, from_= self.incoming, to=self.outgoing)
        return None
        



def nextQuestion (instance=None, messsage=None, db=None):
    print('next question')

def previousQuestion (instance=None, messsage=None, db=None):
    print('previous question')

def statechange (instance=None, messsage=None, db=None):
    print('state change')

def closeSocket(self):
    # Remove client from the clients list and broadcast leave message
    self.participants.remove(self)
    data = {'event' : 'serverMessage', 'data' : '{} has left'.format(self.session.session_id)}
    self.broadcast(self.participants, data)
from tornado import gen

@gen.coroutine
def nextQuestion (con,appState,msg=None):
    print('next question')

@gen.coroutine
def previousQuestion (con,appState,msg=None):
    print('previous question')

@gen.coroutine
def stateChange (con,appstate,msg=None):
    appstate.state = msg['newState']
    yield appstate.save()
    con.broadcast(con.participants, msg)

@gen.coroutine
def closeSocket(self):
    # # Remove client from the clients list and broadcast leave message
    # self.participants.remove(self)
    # data = {'event' : 'serverMessage', 'data' : '{} has left'.format(self.session.session_id)}
    # self.broadcast(self.participants, data)
    pass
from  tornado.web import RequestHandler
from tornado import gen
from sockjs.tornado import SockJSConnection
import json
from  mongo_db import State
import socketEvents


class Home(RequestHandler):

    def get(self):
        self.render('index.html')


class ChatConnection(SockJSConnection):
    """Chat connection implementation"""
    participants = set()

    def __initEvent(self,appstate,msg=None):
        event = getattr(socketEvents, msg['event'])
        event(self, appstate, msg)

    @gen.coroutine
    def on_open(self, info):
        appState = yield State.objects.get('580e67ba61d3661b3953ebba')

        clientJoinedData = {
            'event' : 'serverMessage',
            'message' : '{} has joined'.format(self.session.session_id),
        }
        self.broadcast(self.participants, clientJoinedData)

        msg = {
            'event' : 'clientInit',
            'questionIndex' : appState.questionIndex,
            'numOfQuestions' : appState.numberOfQuestions,
            'state' : appState.state
        }
        self.broadcast([self], msg)
        self.participants.add(self)

    @gen.coroutine
    def on_message(self, message):
        msg = json.loads(message)
        appState = yield State.objects.get('580e67ba61d3661b3953ebba')

        self.__initEvent(appState, msg)

    def on_close(self):
        self.participants.remove(self)
        data = {'event': 'serverMessage', 'data': '{} has left'.format(self.session.session_id)}
        self.broadcast(self.participants, data)




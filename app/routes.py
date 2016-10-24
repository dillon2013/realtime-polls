import tornado.web
import tornado.websocket
from tornado import gen
import pprint
import sockjs.tornado
import json
from  mongo_db import State
import SocketEvents


class Home(tornado.web.RequestHandler):

    def get(self):
        self.render('index.html')

class Users(tornado.web.RequestHandler):
    def get(self):
        pass

class ChatConnection(sockjs.tornado.SockJSConnection):
    """Chat connection implementation"""
    # Class level variable
    participants = set()

    @staticmethod
    def handle_all_users(result):
        print('found all users')

    @gen.coroutine
    def on_open(self, info):

        appState = yield State.objects.get('580e67ba61d3661b3953ebba')
        # appState = data[0]
        print(appState)

        # # Send existing clients message that someone joined
        clientJoinedData = {
            'event' : 'serverMessage',
            'message' : '{} has joined'.format(self.session.session_id),
        }
        self.broadcast(self.participants, clientJoinedData)

        # Send new client the state of application
        msg = {
            'event' : 'clientInit',
            'questionIndex' : appState.questionIndex,
            'numOfQuestions' : appState.numberOfQuestions,
            'state' : appState.state
        }
        self.broadcast([self], msg)
        # #
        # # # yield mongo_db.db.state.update({},{'$push':{'participants':self.session.session_id}})
        # # self.participants.add(self)

    @gen.coroutine
    def on_message(self, message):
        msg = json.loads(message)
        # pprint.pprint(dir(self))




        if msg['event'] == 'nextQuestion':
            pass
            # SocketEvents.nextQuestion()

            # questionIndex =  yield mongo_db.db.state.find({{}:{'questionIndex':1}})

            # if msg['questionIndex'] + 1 < ChatConnection.numOfQuestions:
            #     msg['previousQuestion'] = questionIndex
            #     questionIndex += 1
            #     msg['questionIndex'] = questionIndex
            #     yield mongo_db.db.state.update({},{'$inc':{'questionIndex':1}})
            #     self.broadcast(self.participants, msg)

        elif msg['event'] == 'previousQuestion':
            SocketEvents.previousQuestion()
            # if msg['questionIndex']  > 0:
            #     msg['previousQuestion'] = ChatConnection.questionIndex
            #     ChatConnection.questionIndex -= 1
            #     msg['questionIndex'] = ChatConnection.questionIndex
            #     self.broadcast(self.participants, msg)

        elif msg['event'] == 'stateChange':
            SocketEvents.statechange()
            ChatConnection.state = msg['newState']

            # pprint.pprint(msg)
            self.broadcast(self.participants, msg)

        else:
            self.broadcast(self.participants, msg)


    def on_close(self):
        SocketEvents.closeSocket(self)
        # mongo_db.db.state.update({},{'$pull':{'participants':self.session.session_id}})
        # # Remove client from the clients list and broadcast leave message
        self.participants.remove(self)
        # data = {'event' : 'serverMessage', 'data' : '{} has left'.format(self.session.session_id)}
        self.broadcast(self.participants, data)


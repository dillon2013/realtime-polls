import tornado.web
import tornado.websocket
import pprint
import sockjs.tornado
import json

global questionIndex


class Home(tornado.web.RequestHandler):

    def get(self):
        # pprint.pprint(self.__dict__)
        # pprint.pprint(dir(self))
        # self.set_header('firstname', 'dillons')
        self.render('index.html')

class Users(tornado.web.RequestHandler):
    def get(self):

        users = {'users' : [{
            'name' : 'dillon',
            'age' : 29
        },{
            'name' : 'domonique',
            'age' : 29
        }]}

        self.write(users)

class ChatConnection(sockjs.tornado.SockJSConnection):
    """Chat connection implementation"""
    # Class level variable
    participants = set()
    questionIndex = 0
    numOfQuestions = 2
    state = 'index'

    def on_open(self, info):
        # Send existing clients message that someone joined
        clientJoinedData = {
            'event' : 'serverMessage',
            'message' : '{} has joined'.format(self.session.session_id),
        }
        self.broadcast(self.participants, clientJoinedData)

        # Send new client the state of application
        msg = {
            'event' : 'clientInit',
            'questionIndex' : ChatConnection.questionIndex,
            'numOfQuestions' : ChatConnection.numOfQuestions,
            'state' : ChatConnection.state
        }
        self.broadcast([self], msg)

        #add client to participants
        self.participants.add(self)

    def on_message(self, message):
        msg = json.loads(message)

        if msg['event'] == 'nextQuestion':
            if msg['questionIndex'] + 1 < ChatConnection.numOfQuestions:
                msg['previousQuestion'] = ChatConnection.questionIndex
                ChatConnection.questionIndex += 1
                msg['questionIndex'] = ChatConnection.questionIndex
                self.broadcast(self.participants, msg)

        elif msg['event'] == 'previousQuestion':
            if msg['questionIndex']  > 0:
                msg['previousQuestion'] = ChatConnection.questionIndex
                ChatConnection.questionIndex -= 1
                msg['questionIndex'] = ChatConnection.questionIndex
                self.broadcast(self.participants, msg)

        elif msg['event'] == 'stateChange':
            ChatConnection.state = msg['newState']
            self.broadcast(self.participants, msg)

        else:
            self.broadcast(self.participants, msg)


    def on_close(self):
        # Remove client from the clients list and broadcast leave message
        self.participants.remove(self)
        data = {'event' : 'serverMessage', 'data' : '{} has left'.format(self.session.session_id)}
        self.broadcast(self.participants, data)

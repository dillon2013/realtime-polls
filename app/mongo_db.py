# import motor.motor_tornado
#
# client = motor.motor_tornado.MotorClient('localhost', 27017)
# db = client['polls']


from motorengine.document import Document
from motorengine.fields import StringField, DateTimeField, IntField, ListField

class State(Document):
    state = StringField(required=True)
    questionIndex = IntField(required=True)
    numberOfQuestions = IntField()
    participants = ListField(StringField())

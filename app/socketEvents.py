from tornado import gen

@gen.coroutine
def nextQuestion (this,appState,msg):
    if msg['questionIndex'] + 1 < appState.numberOfQuestions:
        msg['previousQuestion'] = appState.questionIndex
        appState.questionIndex += 1
        msg['questionIndex'] = appState.questionIndex
        yield appState.save()
        this.broadcast(this.participants, msg)

@gen.coroutine
def previousQuestion (this,appState,msg):
    if msg['questionIndex'] > 0:
        msg['previousQuestion'] = appState.questionIndex
        appState.questionIndex -= 1
        msg['questionIndex'] = appState.questionIndex
        yield appState.save()
        this.broadcast(this.participants, msg)


@gen.coroutine
def stateChange (this,appstate,msg):
    appstate.state = msg['newState']
    yield appstate.save()
    this.broadcast(this.participants, msg)

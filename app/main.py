import tornado.ioloop
import tornado.web
import os
import routes
import tornado.log
import sockjs.tornado
import pprint
import motor.motor_tornado

client = motor.motor_tornado.MotorClient('localhost', 27017)
db = client['polls']


tornado.log.enable_pretty_logging()

port = 8888
settings = {
    "autoreload" : True,
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
    "static_hash_cache" : False,
    "compiled_template_cache" : False,
    "db" : db,
}
ChatRouter = sockjs.tornado.SockJSRouter(routes.ChatConnection, '/ws')

def make_app():
    return tornado.web.Application([
        (r"/api/users", routes.Users),
        (r"/?\w*", routes.Home)
    ] + ChatRouter.urls, **settings)

if __name__ == "__main__":
    print('server listening on port ' + str(port))
    app = make_app()
    app.listen(port)
    tornado.ioloop.IOLoop.instance().start()
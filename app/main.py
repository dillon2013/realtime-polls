import tornado.ioloop
import tornado.web
import os
import routes
import tornado.log
import sockjs.tornado
from motorengine import connect

tornado.log.enable_pretty_logging()

port = 8888
settings = {
    "autoreload": True,
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
    "static_hash_cache": False,
    "compiled_template_cache": False
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
    io_loop = tornado.ioloop.IOLoop.instance()
    connect("polls", host="localhost", port=27017, io_loop=io_loop)
    io_loop.start()




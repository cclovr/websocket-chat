import os
import sys
import tornado.ioloop
import tornado.web
import handlers

def make_app(bundle_path, debug):
    return tornado.web.Application(
      debug=debug,
      handlers=[
        (r"/api/listen_connection_users", handlers.ConnectionUsersWebsocket)
      ]
    )


if __name__ == "__main__":
    debug = False
    bundle_path = 'http://localhost:8888/'
    app = make_app(bundle_path, debug)
    app.listen(8888)
    print('http://localhost:8888')
    tornado.ioloop.IOLoop.current().start()

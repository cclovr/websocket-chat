import os
import sys
import tornado.ioloop
import tornado.web
import tornado.auth
import handlers

def make_app(bundle_path, debug):
    return tornado.web.Application(
      template_path=os.path.join(os.path.dirname(__file__), "views"),
      static_path=os.path.join(os.path.dirname(__file__), "public"),
      debug=debug,
      handlers=[
        (r"/api/listen_connection_users", handlers.ConnectionUsersWebsocket)
        (r"/api/connect_users_to_chat", handlers.ConnectUsersToChatWebsocket)
      ],
    )


if __name__ == "__main__":
    debug = False
    bundle_path = 'http://localhost:8888/'
    app = make_app(bundle_path, debug)
    app.listen(8888)
    print('http://localhost:8888')
    tornado.ioloop.IOLoop.current().start()

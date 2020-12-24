import tornado.web
import json
from random import *
import tornado.websocket
import tornado.escape
import tornado.auth
import logging
from tornado.options import define, options

activeUsers = []
print('1', activeUsers)

class BaseHandler(tornado.web.RequestHandler):
  def set_default_headers(self, *args, **kwargs):
    self.set_header("Access-Control-Allow-Origin", "*")
    self.set_header("Access-Control-Allow-Methods", "POST, GET, OPTIONS")
    self.set_header("Access-Control-Allow-Headers",
                    "Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With")

  def options(self, *args, **kwargs):
    self.set_header('Access-Control-Allow-Headers', '*')
    self.set_header('Access-Control-Allow-Methods', '*')


class RandomHandler(BaseHandler):
    def get(self):
        self.write({'randomNumber': '111111'})


# class LoginHandler(BaseHandler):
#     def post(self):
#         username = tornado.escape.json_decode(self.request.body)
#         activeUsers.append(username)


class ConnectionUsersWebsocket(BaseHandler, tornado.websocket.WebSocketHandler):
    waiters = set()

    def get_compression_options(self):
        # Non-None enables compression with default options.
        return {}

    def on_message(self, message):
        # username = tornado.escape.json_decode(message)
        # activeUsers.append(tornado.escape.json_decode(message))
        # print(activeUsers)
        self.write_message(message=tornado.escape.json_decode(message))

    def check_origin(self, origin):
        return True

    def open(self):
        ConnectionUsersWebsocket.waiters.add(self)

    def on_close(self):
        ConnectionUsersWebsocket.waiters.remove(self)

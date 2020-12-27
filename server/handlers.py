import tornado.web
import json
from random import *
import tornado.websocket
import tornado.escape
import tornado.auth
import logging
import socketio
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


class OptionsWebsocket(BaseHandler, tornado.websocket.WebSocketHandler):
    waiters = set()

    def get_compression_options(self):
        return {}

    def check_origin(self, origin):
        return True

    def open(self):
        OptionsWebsocket.waiters.add(self)

    def on_close(self):
        OptionsWebsocket.waiters.remove(self)


class ConnectionUsersWebsocket(OptionsWebsocket):
    def on_message(self, message):
        self.write_message(message=tornado.escape.json_decode(message))


class ConnectUsersToChatWebsocket(OptionsWebsocket):
    def on_message(self, message):
        self.write_message(message=tornado.escape.json_decode(message))

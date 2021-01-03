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
    def get_compression_options(self):
        return {}

    def check_origin(self, origin):
        return True


class ConnectionUsersWebsocket(OptionsWebsocket):
    waitersNode = set()
    cache = []
    cache_size = 200

    def open(self):
        ConnectionUsersWebsocket.waitersNode.add(self)

    def on_close(self):
        ConnectionUsersWebsocket.waitersNode.remove(self)

    @classmethod
    def update_cache(cls, chat):
        cls.cache.append(chat)
        if len(cls.cache) > cls.cache_size:
            cls.cache = cls.cache[-cls.cache_size:]

    @classmethod
    def send_updates(cls, chat):
        logging.info("sending message to %d waiters", len(cls.waitersNode))
        for waiter in cls.waitersNode:
            try:
                waiter.write_message(chat)
            except:
                logging.error("Error sending message", exc_info=True)

    def on_message(self, message):
        ConnectionUsersWebsocket.update_cache(message)
        ConnectionUsersWebsocket.send_updates(message)


class ConnectUsersToChatWebsocket(OptionsWebsocket):
    waiters = set()
    cache = []
    cache_size = 200

    @classmethod
    def update_cache(cls, chat):
        cls.cache.append(chat)
        if len(cls.cache) > cls.cache_size:
            cls.cache = cls.cache[-cls.cache_size:]

    @classmethod
    def send_updates(cls, chat):
        logging.info("sending message to %d waiters", len(cls.waiters))
        for waiter in cls.waiters:
            try:
                waiter.write_message(chat)
                ChatSocketHandler.update_cache(chat)
                ChatSocketHandler.send_updates(chat)
            except:
                logging.error("Error sending message", exc_info=True)

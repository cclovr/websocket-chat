import tornado.web
import json
from random import *
import tornado.websocket
import tornado.escape
import tornado.auth
import logging
import socketio
from tornado.options import define, options


class OptionsWebsocket(tornado.websocket.WebSocketHandler):
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
        for waiterNode in cls.waitersNode:
            try:
                waiterNode.write_message(chat)
            except:
                logging.error("Error sending message", exc_info=True)

    def on_message(self, message):
        ConnectionUsersWebsocket.update_cache(message)
        ConnectionUsersWebsocket.send_updates(message)

#wtfapp/events.py

import os
from time import localtime, strftime
from flask import request
from flask_socketio import emit, send

from .extentions import socketio

users = {}


@socketio.on('message')
def message(data):
    print(f'\n\n{data}\n\n')
    send(data)      # broadcastthe pre-defined bucket called 'message' to all the clients connected at the clients' side
    emit('some-event', '這是從服務器發給客戶端的 custom event message!')  # send to the customed client event bucket from server
    # send({'msg': data['msg'], 'username' : data['username'], 'time_stamp' : strftime('%b-%d %I:%M%p', localtime())}, room=data['room']) # type: ignore


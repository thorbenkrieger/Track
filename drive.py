from flask import Flask
import socketio
import eventlet

sio = socketio.Server()
app = Flask(__name__) #'__main__'

@sio.on('connect') #message, disconnect
def connect(sid,environ):
    print('Connected')



if __name__ == '__main__':
    app = socketio.Middleware(sio, app)
    eventlet.wsgi.server(eventlet.listen(('', 4567)), app)
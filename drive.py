from flask import Flask
from flask_socketio import SocketIO
#import socketio
import eventlet

#sio = socketio.Server()
app = Flask(__name__) #'__main__'
socketio = SocketIO(app)


@socketio.on('*')  
def catch_all(event, data):
    print("Catch_all")

@socketio.on('connect')  
def connection(sid, environ):
    print('connect ', sid)

@socketio.on('connection')  
#@sio.on('connection') 
def connect(sid,environ):
    print('Connected')
    send_control(0,1)

def send_control(steering_angle, throttle):
    sio.emit('steer', data = {
        'steering_angle': steering_angle.__str__(),
        'throttle' : throttle.__str__()
    })


if __name__ == '__main__':
    print('Starting app')
    socketio.run(app)
   # app = socketio.WSGIApp(sio, app)
   # eventlet.wsgi.server(eventlet.listen(('', 4567)), app)


from flask import Flask
import socketio
import eventlet

sio = socketio.Server()
app = Flask(__name__) #'__main__'


@sio.on('*')
def catch_all(event, data):
    print(event)
    
@sio.event
def connect():
    print('Connected')
    send_control(0,1)  
     
#@sio.on('connect') 
#def connect(sid,environ):
#    print('Connected')
#    send_control(0,1)

def send_control(steering_angle, throttle):
    sio.emit('steer', data = {
        'steering_angle': steering_angle.__str__(),
        'throttle' : throttle.__str__()
    })


if __name__ == '__main__':
    app = socketio.Middleware(sio, app)
    eventlet.wsgi.server(eventlet.listen(('', 4567)), app)


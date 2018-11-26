from flask import Flask, render_template
from flask_socketio import SocketIO
import json

import uh_light as UhLight

app = Flask(__name__)
app.config['SECRET_KEY'] = 'test'
socketio = SocketIO(app)

# ROUTES
@app.route('/')
def index():
	return render_template('index.html')

#EVENTS
@socketio.on('connect')
def connect():
	data = {
		'button': [
			['power', UhLight.power]
		],
		'r':UhLight.color['r'],
		'g':UhLight.color['g'],
		'b':UhLight.color['b']
	}

	socketio.emit('connect_conf', json.dumps(data))

@socketio.on('message')
def handle_color(data):
	UhLight.setlight(data['r'], data['g'], data['b'])

@socketio.on('toggle_button')
def toggle_button(data):
	button = data['button']
	value = data['value']
	if button == 'power':
		if value == 1:
			UhLight.turnOn()
		else:
			UhLight.turnOff()

@socketio.on('print')
def print_data(data):
	print(data)


def run():
	socketio.run(app, host='0.0.0.0', port=80, debug=True)
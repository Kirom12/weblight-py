from flask import Flask, render_template
from flask_socketio import SocketIO
import uh_light as UhLight

app = Flask(__name__)
app.config['SECRET_KEY'] = 'merinac'
socketio = SocketIO(app)

@app.route('/')
def hello_world():
	return render_template('index.html')

@socketio.on('message')
def handle_color(data):
	UhLight.setlight(data['r'], data['g'], data['b'])

def run():
	socketio.run(app, host='0.0.0.0', port=80, debug=True)
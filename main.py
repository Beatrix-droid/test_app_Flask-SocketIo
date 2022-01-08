from flask_socketio import SocketIO, send
from flask import Flask, render_template

app = Flask(__name__)
app.config["SECRET KEY"] = "a_secret!"
socketio = SocketIO(app)


# defining a message:

@socketio.on("message")
def handleMessage(msg):
	print("message: " + msg)
	# broadcast = true lets everyone in the chatroom see the message
	send(msg, broadcast=True)

@app.route('/')
def hello_world():
	return render_template("index.html")

if __name__ == "__main_":
	# instead of app.run()
	# socket io takes the typicdcal flask app and wraps it around the socketio functionilty
	socketio.run(app)
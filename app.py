# app.py

from wtfapp import create_app
from wtfapp.extentions import socketio

app = create_app()

# if __name__ == '__main__':
# app.run(debug=True)
socketio.run(app,debug=True)
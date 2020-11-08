from flask import *
from flaskwebgui import *

app = Flask(__name__)

ui = FlaskUI(app)

@app.route('/')
def hello_world():
    return render_template('PokerApp.html')

ui.run()
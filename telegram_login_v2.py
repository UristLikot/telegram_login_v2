from flask import Flask, render_template,request
import tgchanbot
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


if __name__ == '__main__':
    tgchanbot.start_bot()
    app.run(host="localhost", port=8001, debug=True)
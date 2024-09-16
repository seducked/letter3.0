from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')

def root():
    return render_template('index.html')

@app.route('/show')
def show():
    message = request.args['message']
    return render_template('display.html', message = message)
app.run()

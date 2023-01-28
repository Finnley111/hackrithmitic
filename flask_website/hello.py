from flask import Flask
import csv

app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'hi world!'

if __name__ == "__main__":
    app.run()

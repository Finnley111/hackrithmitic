from flask import Flask

app = Flask(__name__)
@app.route('/')
def hello_world():
    return parse_email()
    return 'hi world!'

if __name__ == "__main__":
    app.run()

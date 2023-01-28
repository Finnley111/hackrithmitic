from flask import Flask
import model
import new_email

def test():
    email = '''Hi Finnley,

    Congratulations, you have passed the screening stage for the Data Scientist (Risk Research) Intern position and will move on to the next step of the process, our technical test.

    The test will take at most 120 minutes. Please ensure you use the same email on the test as you did on your application so we can credit you with your results. You will receive an invitation from HackerRank shortly after receiving this email.

    Please ensure you take the test within 72 hours of receiving it. The system takes some time to send the test link, but if you do not receive it by the end of the day, please respond to this email, and I will re-send it.

    Any questions? Please join our internship LinkedIn Network for the fastest response time, and post your questions in the group.

    Best of luck!

    Eleanor Hawkins
    Campus Recruitment Team
    GeoComply'''

    test = new_email.email_data(email)
    return str(model.get_result(test))

app = Flask(__name__)
@app.route('/')
def hello_world():
    return test()
    return 'hi world!'

if __name__ == "__main__":
    app.debug = True
    app.run()


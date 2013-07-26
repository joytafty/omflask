import urllib
import re
from flask import Flask, request
import twilio.twiml
app = Flask(__name__)
 
 
def submit_to_google_form(formkey, keyword, email, number):
    google_form = "https://docs.google.com/spreadsheet/" \
                  "formResponse?formkey=%s&ifq" % formkey
    params = urllib.urlencode({'entry.0.single': keyword,
                               'entry.1.single': email,
                               'entry.2.single': number,
                               'pageNumber': '0',
                               'backupCache': '',
                               'submit': 'Submit'})
    f = urllib.urlopen(google_form, params)
    result = f.read()
    if re.search(r'Create your own form', result):
        return True
    return False

@app.route("/")
def note():
    return "Send SMS to the /spreadsheet/<formkey> route"
 
 
@app.route("/spreadsheet/<formkey>", methods=['GET', 'POST'])
def spreadsheet(formkey):
    resp = twilio.twiml.Response()
    body = request.form['Body']
    space = re.compile(r' ')
    if space.findall(body):
        (keyword, email) = body.split(' ', 1)
    else:
        keyword = body
        email = ''
    number = request.form['From']
    # example formkey: "xXXXxXXxxXXXX1XXxXXxXXXXXxxxXXX1XX"
    if submit_to_google_form(formkey, keyword, email, number):
        resp.sms("Thank you for subscribing to the '%s' keyword." % keyword)
    else:
        resp.sms("We're sorry, we're having issues processing SMS right now. "
                 "Please try later")
    return str(resp)
 
if __name__ == "__main__":
    app.run()
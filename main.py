from regex import check_regex
from flask import Flask
from dnschecker import dnscheck
from mailbox import mailboxcheck
from freemailprovider import freemailpro
from rolebased import rolemails
from accept_all import checkacceptall
import time

app = Flask(__name__)


@app.route("/")
def index():
    return {
        'message': "Welcome To Email Verification Service V1.0 ."
    }


@app.route("/api/v1/<email>")
def verification(email):
    start_time = time.time()

    regex_valid = check_regex(email)

    if regex_valid:
        splits = email.split('@')
        domain = splits[1]
        user = splits[0]
        mx_record = dnscheck(domain)
        state = mailboxcheck(email, mx_record)
        duration = time.time() - start_time
        free = freemailpro(domain)
        role = rolemails(user)
        accpt = checkacceptall(domain, mx_record)

        if accpt:
            state = "risky"
        return {
            'accept_all': accpt,
            'disposable': free,
            'domain': domain,
            'duration': duration,
            'email': email,
            'free': free,
            'mx_record': mx_record,
            'reason': 'Email ' + state,
            'role': role,
            'state': state,
            'user': user
        }
    else:
        return {
            'accept_all': False,
            'disposable': True,
            'domain': 'unknown',
            'duration': 0.06,
            'email': email,
            'free': 'unknown',
            'mx_record': 'unknown',
            'reason': 'Invalid Email Syntax',
            'role': 'unknown',
            'state': 'undeliverable',
            'user': 'unknown'

        }


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    app.run(debug=True)

# pip install flask
# pip install dns

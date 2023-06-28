
from flask import render_template, redirect, request, session
from flask_app.models.user import User
from flask_app import app

from email.message import EmailMessage
import ssl
import smtplib

#######################################################
#                 loading start
#######################################################
@app.route("/")
def register_login():
    return render_template ("home.html")
#######################################################


#######################################################
##                  emailer test
#######################################################
@app.route("/sendemail", methods=["POST"])
def sendemail():
    auto_mailer = "noreplybarleyandbrew@gmail.com"
    receiver1 = "manager@barleyanddbrew.com"
    receiver2 = "mike@barleyanddbrew.com"

    with open("flask_app/controllers/test.txt", "r") as f:
        password = f.read()

    sender = request.form["email"]
    subject = request.form["subject"]

    description = f"""
    Email: {sender}
    Subject Type: {subject}
    Description: {request.form["description"]}
    """

    msg = EmailMessage()
    msg["From"] = sender
    msg["subject"] = f"no-reply QCC Submission - {subject}"
    msg.set_content(description)
    
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
        smtp.login(auto_mailer, password)
        smtp.sendmail(auto_mailer, receiver1, msg.as_string())
        smtp.sendmail(sender, receiver2, msg.as_string())
        smtp.quit()
        print("message successful")

    return redirect("/")


#######################################################

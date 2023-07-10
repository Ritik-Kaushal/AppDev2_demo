from instance.mail import mail
from instance.app import app
from flask_mail import Message
import os



def sendMail(RECEIVER_ADDRESS,SUBJECT,MESSAGE,ATTACHMENT=None,mime_type = "application/pdf"):
    try:
       
        msg = Message(recipients=[RECEIVER_ADDRESS],
                    sender=app.config['MAIL_USERNAME'],
                    body=MESSAGE,
                    subject=SUBJECT)
        if ATTACHMENT :
            with app.open_resource(ATTACHMENT) as fp:
                if mime_type == "application/pdf" :
                    msg.attach(f"{RECEIVER_ADDRESS}_report.pdf",mime_type , fp.read())
                elif mime_type == "application/x-zip" :
                    msg.attach(f"{RECEIVER_ADDRESS}_exported.zip",mime_type , fp.read())
                elif mime_type == "text/csv":  # Add this block for .csv files
                    msg.attach(f"{RECEIVER_ADDRESS}_data.csv", mime_type, fp.read())


        mail.send(msg)
        return True
    except Exception as e:
        print(e)
        return False
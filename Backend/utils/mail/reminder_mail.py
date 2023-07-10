from application.models import Testimonial,User
from utils.mail.mail import sendMail


def send_remainder_emails():
    try:

        # Get the testimonials which are not approved.
        testimonials = Testimonial.query.filter_by(approved=False).all()

        # Get the admin
        admin= User.query.filter_by(role='ADMIN').first()

        # Set the message to send
        message = ""
        if len(testimonials) == 0:
            message = "Great !!! You don't have any testimonials to approve."
        else:
            message = "You have {0} testimonials to approve.".format(len(testimonials))
        
        # Send the email to admin 
        res = sendMail(admin.email,"Reminder for approving testimonials",message)
        return res
    except:
        return False


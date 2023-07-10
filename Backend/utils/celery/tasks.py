from instance.celery import cel
from celery.schedules import crontab


@cel.on_after_configure.connect
def setup_periodic_tasks(sender,**kwargs):
    pass
    # sender.add_periodic_task(crontab(hour=18, minute=0),remainder_emails.s(),name="A remainder email to all those who have not updated the logs today")
    sender.add_periodic_task(60,remainder_emails.s(),name="A remainder email to approve testimonials.")


from utils.mail.reminder_mail import send_remainder_emails
@cel.task(name="send remainder emails")
def remainder_emails():
    res = send_remainder_emails()
    
    if(res): return 'Successfully Sent'
    else : return 'Failed to send'

from utils.mail.export_data import export_testimonial_data
@cel.task(name="export")
def export_data():
    res = export_testimonial_data()
        
    if(res): return [True,'Successfully Exported']
    else : return [False,'Failed to export']


import csv
import os
from application.models import Testimonial,User
from utils.mail.mail import sendMail


def export_testimonial_data():
    try:
        # Get the testimonials to export
        testimonials = Testimonial.query.all()

        # Get the admin from database
        admin = User.query.filter_by(role='ADMIN').first()

        # Change the working directory to instance
        os.chdir('instance')

        # File to store the testimonials in form of csv
        file_path = "testimonial_export.csv"

        # Write the content in the file
        with open(file_path, 'w', newline='') as csv_file:
            fieldnames = ['id', 'content','approved','user_id']  # Replace with the actual column names in your Testimonial table
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()

            for testimonial in testimonials:
                writer.writerow({
                    'id': testimonial.id, 
                    'content': testimonial.content, 
                    'approved' : testimonial.approved, 
                    'user_id':testimonial.user_id
                })

        # Send the email to admin with the csv file in atatchment
        res = sendMail(admin.email,"Testimonial Exports","The testimonials has been exported and attached below.",file_path,"text/csv")
        return res
    except Exception as e:
        print(e)
        return False


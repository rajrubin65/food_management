import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# Email configuration
sender_email = "rubincomercial@gmail.com"
sender_password = "hpsf lzji lngt lkro"
recipient_email = "rajrubin072@gmail.com"
subject = "The Food Management Report"
message_body = "Food Management Full Report"

# Create a MIME object for the email message
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = recipient_email
msg['Subject'] = subject


def send_email():
    # Attach the message body
    msg.attach(MIMEText(message_body, 'plain'))

    # Attach a CSV file (change 'data.csv' to the path of your CSV file)
    csv_filename = 'data.csv'
    attachment = open(csv_filename, 'rb')
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % csv_filename)
    msg.attach(part)

    # Establish a connection to the SMTP server (Gmail in this example)
    try:
        smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
        smtp_server.starttls()
        smtp_server.login(sender_email, sender_password)
        
        # Send the email
        smtp_server.sendmail(sender_email, recipient_email, msg.as_string())
        
        # Close the SMTP server connection
        smtp_server.quit()
        print("Email with CSV attachment sent successfully")
    except Exception as e:
        print("An error occurred:", str(e))

import smtplib
#from email.MIMEMultipart import MIMEMultipart
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# simple mail transfer protocol library
#Multipurpose Internet Mail Extension

fromaddr = 'hoffmann.vitali@gmail.com'
toaddr = 'angi.h.ah@gmail.com'
text = 'testText'
username = 'hoffmann.vitali@gmail.com'
password = 'YouRkingdom<3come!'

msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = 'Test'
msg.attach(MIMEText(text))

def send_it():
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(username, password)
    server.sendmail(fromaddr, toaddr, msg.as_string())
    server.quit()

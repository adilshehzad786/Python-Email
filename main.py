from email.mime.multipart import MIMEMultipart
from email.mime.text import  MIMEText
from email.mime.image import MIMEImage
from pathlib import Path

from string import Template

import smtplib
temp=Template(Path("template.html").read_text())

message=MIMEMultipart()
message["From"]="youremail@yourmail.com"
message["To"]="youremail@yourmail.com"
message["Subject"]="HEllo From Python"
body=temp.substitute({"Name":"John"})
message.attach(MIMEText(body,"html"))
message.attach(MIMEImage(Path("Yourimage.JPG").read_bytes()))

with smtplib.SMTP(host="smtp.mailgun.org",port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("youremail@yourmail.com","yourpassword") #dontshare your password
    smtp.send_message(message)
    print("Send")






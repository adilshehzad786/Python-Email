from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path

from string import Template

import smtplib
from email.mime.base import MIMEBase
from email import encoders


temp = Template (Path("template.html").read_text ())
subject='Subject Here'
message = MIMEMultipart ()
message["From"] = "toco@net1mail.com"
message["To"] = "*****5a786@gmail.com,******@gmail.com"
message["Subject"] = subject

body = temp.substitute ({"Name": "John"})
message.attach (MIMEText (body , "html"))
#message.attach (MIMEImage (Path ("Yourimage.JPG").read_bytes ()))
filename='filename.txt'
attachment  =open(filename,'rb')

part = MIMEBase('application','octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition',"attachment; filename= "+filename)

message.attach(part)
text = message.as_string()

with smtplib.SMTP (host="smtp.mailgun.org" , port=587) as smtp: #use free  smtp.gmail.com 
    print ("Sending Email" ,"To", message["To"],"using",smtp)
    smtp.ehlo ()
    smtp.starttls ()
    smtp.login ("*********************************.mailgun.org" , "**********************************")  # dontshare your password
    smtp.send_message (message)
    print("Job Done ")
#smtp.quit()





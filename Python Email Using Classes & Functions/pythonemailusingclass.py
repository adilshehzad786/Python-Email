import smtplib
from email.mime.text import MIMEText

class Email_Server:

	def __init__(self,username,password):

		self.server=smtplib.SMTP('smtp.mailgun.org:587')
		self.server.starttls()
		self.server.login(username,password)

	def __enter__(self):
		return self.server

	def __exit__(self,type,value,traceback):
		self.server.quit()

def Send_Mail(server,from_address,to_address,subject,body):

	msg=MIMEText(body)
	msg['subject']=subject
	msg['From']=from_address
	msg['To']=to_address

	server.sendmail(from_address,[to_address],msg.as_string())

from_address = 'toco@net1mail.com'  
to_address= 'sender_email@mailgun.org'  
subject= 'subject'
body = 'Hello'    
  
# Credentials  
username = '#################.mailgun.org' 
password = 'Password here' 
		
with Email_Server(username, password) as server:
	Send_Mail(server, from_address, to_address, subject, body)
	print("Send")



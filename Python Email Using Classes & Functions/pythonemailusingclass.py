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
to_address= 'ufoneu5a786@gmail.com'  
subject= 'subject'
body = 'Hello'    
  
# Credentials  
username = 'postmaster@sandbox724f4a3fb5ab459f873f57a67f922f40.mailgun.org' 
password = '858195c536b3d5fb2b40121d4642d1bc-baa55c84-c59b7d2e' 
		
with Email_Server(username, password) as server:
	Send_Mail(server, from_address, to_address, subject, body)
	print("Send")



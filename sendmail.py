import time
import smtplib
 
TO = raw_input("Enter your partner email: ")
GMAIL_USER = raw_input("Enter your gmail account: ")
GMAIL_PASS = raw_input("Enter your gmail password: ")
 
SUBJECT = raw_input("Enter your Email subject: ")
TEXT = raw_input("Enter your Email messages: ")
  

 
def send_email():
    print("Sending Email")
    smtpserver = smtplib.SMTP("smtp.gmail.com",587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo()
    smtpserver.login(GMAIL_USER, GMAIL_PASS)
    header = 'To:' + TO + '\n' + 'From: ' + GMAIL_USER
    header = header + '\n' + 'Subject:' + SUBJECT + '\n'
    print header
    msg = header + '\n' + TEXT + ' \n\n'
    smtpserver.sendmail(GMAIL_USER, TO, msg)
    smtpserver.close()

counter = 0  
while True:
    
    print("Send messages number",counter)
    send_email()
    counter = counter + 1
    time.sleep(2)
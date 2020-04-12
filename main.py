import os
import smtplib
import time
import schedule
from dotenv import load_dotenv
load_dotenv()

user_email = os.getenv('user_email')
user_password = os.getenv('user_password')

test_email = os.getenv('test_email')
professor_email = os.getenv('professor_email')


def send_email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(user_email, user_password)

    email_subject = 'EMAIL SUBJECT'
    email_text = 'EMAIL CONTENT'
    message = 'Subject: {}\n\n{}'.format(email_subject, email_text)

    server.sendmail(user_email, user_email, message)
    server.quit()


schedule.every().day.at("00:57").do(send_email)

while True:
    schedule.run_pending()
    time.sleep(1)


# import datetime as dt
# send_time = dt.datetime(2020, 4, 12, 23, 4, 0)
# time.sleep(send_time.timestamp() - time.time())

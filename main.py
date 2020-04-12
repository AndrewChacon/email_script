import os
import smtplib
import time
import schedule
from random import randrange
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()

user_email = os.getenv('user_email')
user_password = os.getenv('user_password')
test_email = os.getenv('test_email')
professor_email = os.getenv('professor_email')

check_in_subject = os.getenv('check_in_subject')
check_in_content = os.getenv('check_in_content')
check_in_email = 'Subject: {}\n\n{}'.format(check_in_subject, check_in_content)

check_out_subject = os.getenv('check_out_subject')
check_out_content = os.getenv('check_out_content')
check_out_email = 'Subject: {}\n\n{}'.format(
    check_out_subject, check_out_content)


def confirm_email():
    print("Email Sent At:")
    print(datetime.now(tz=None))
    print("")


def send_email(message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(user_email, user_password)
    server.sendmail(user_email, user_email, message)
    server.quit()
    confirm_email()


print('\nServer Is Up And Running\n')

schedule.every().tuesday.at('09:15').do(lambda: send_email(check_in_email))
schedule.every().tuesday.at('11:15').do(lambda: send_email(check_out_email))

schedule.every().thursday.at('09:15').do(lambda: send_email(check_in_email))
schedule.every().thursday.at('11:15').do(lambda: send_email(check_out_email))

while True:
    schedule.run_pending()
    time.sleep(1)

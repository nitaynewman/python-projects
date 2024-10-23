import smtplib
from env import BUISNES_EMAIL, OPEN_PASSWORD

MY_EMAIL = BUISNES_EMAIL
PASSWORD = OPEN_PASSWORD
connection = smtplib.SMTP("smtp.gmail.com", 587)
connection.starttls()
connection.login(user=MY_EMAIL, password=PASSWORD)
connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg='hello')
connection.close()

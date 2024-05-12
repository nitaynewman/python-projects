import smtplib
import datetime as dt
import random
from env import BUISNES_EMAIL, OPEN_PASSWORD, MY_EMAIL

FROM_EMAIL = BUISNES_EMAIL
MY_PASSWORD = OPEN_PASSWORD
TO_EMAIL = MY_EMAIL

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 0:
    with open('quotes.txt', encoding='utf-8') as quotes:
        all_quotes = quotes.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=FROM_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=FROM_EMAIL,
            to_addrs=TO_EMAIL,
            msg=f'Subject: Sunday Motivation\n\n{quote}'.encode('utf-8')  # Encoding the message using UTF-8
        )
        connection.close()
        print('success')

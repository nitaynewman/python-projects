import smtplib
import datetime as dt
import random
import pandas

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
MY_EMAIL = 'nitaybusines@gmail.com'
MY_PASSWORD = 'ghlx gdms ridi qbdz'
NOW = (dt.datetime.now().month, dt.datetime.now().day)

data = pandas.read_csv('birthdays.csv')

birthdays_dict = {
    (data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()
}
if NOW in birthdays_dict:
    person = birthdays_dict[NOW]
    with open('brahot.txt') as wishes:
        all_wishes = wishes.readlines()
        wish = random.choice(all_wishes)
        wish = wish.replace('name', person['name'])

    print(wish)
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f'Subjet: Happy Birthday\n\n{wish}'
        )
        connection.close()
        print('sucses')

# with open('birthday.csv') as birth_data:
#   all_month = birth_data['month']
#   all_days = birth_data['day']

# if NOW.month == all_month and NOW.day == all_days:
#   with open('brahot.txt') as quotes:
#     quotes = quotes.readlines()
#     quote = random.choice(quotes)
#     print(quote)
#     with smtplib.SMTP('smtp.gmail.com') as connection:
#       connection.starttls()
#       connection.login(user=MY_EMAIL, password=MY_PASSWORD)
#       connection.sendmail(
#         from_addr=MY_EMAIL,
#         to_addrs=TO_EMAIL,
#         msg=f'Subject: Happy Birthday\n\n{quote}'
#       )

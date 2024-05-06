import smtplib

MY_EMAIL = "nitaybusines@gmail.com"
PASSWORD = 'ghlx gdms ridi qbdz'
connection = smtplib.SMTP("smtp.gmail.com", 587)
connection.starttls()
connection.login(user=MY_EMAIL, password=PASSWORD)
connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg='hello')
connection.close()

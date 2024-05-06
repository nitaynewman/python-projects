import requests
from bs4 import BeautifulSoup
import smtplib

EMAIL = "nitaybusines@gmail.com"
PASSWORD = "ghlx gdms ridi qbdz"

url = "https://www.amazon.com.tr/SanDisk-SDSSDA-240G-G26-SSD-Plus-240GB/dp/B07621PNWC/ref=sr_1_1?keywords=ssd%2B240" \
      "%2Bgb&qid=1658063784&sprefix=ssd%2B%2Cspecialty-aps%2C108&sr=8-1&th=1"
header = {
    "Accept-Language": "en-US,en;q=0.9,tr;q=0.8,fa;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 "
                  "Safari/537.36",
}

response = requests.get(url=url, headers=header)
response.raise_for_status()
bs = BeautifulSoup(response.text, "lxml")

price_element = bs.select_one("span.a-price-whole")
if price_element:
    price_tl = int(price_element.getText().split(",")[0])
    price_kr = int(bs.select_one("span.a-price-fraction").getText())
    price = price_tl + (price_kr / 100)
    print(price)
else:
    print("Price not found")

product_title_element = bs.select_one("span.a-size-large")
if product_title_element:
    product_title = product_title_element.getText().strip()
    print(product_title)
else:
    print("Product title not found")

# Send email
target_price = 500
if 'price' in locals() and price < target_price:
    connection = smtplib.SMTP("smtp.gmail.com", port=587)
    connection.starttls()
    connection.login(user=EMAIL, password=PASSWORD)
    message = f"{product_title} is now {price}\n{url}"
    receiver_mail = "Receiver Mail"
    connection.sendmail(
        from_addr=EMAIL,
        to_addrs=EMAIL,
        msg=f"Subject:Amazon Price Alert\n\n{message}"
    )
    connection.close()

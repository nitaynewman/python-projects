import requests
from bs4 import BeautifulSoup
import smtplib

# Function to get the price from the AliExpress page
def get_price(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    price_element = soup.find(class_='notranslate')
    if price_element:
        price_text = price_element.get_text()
        price = float(price_text.split('₪')[1].replace(',', ''))  # Remove currency symbol and commas
        return price
    else:
        print("Price element not found")
        return None

# URL of the AliExpress product
URL = "https://he.aliexpress.com/item/32839489621.html?spm=a2g0o.productlist.main.3.2e14mcsamcsaZY&algo_pvid=18419ecb-4de1-4fde-b04f-70bf9263d8d1&algo_exp_id=18419ecb-4de1-4fde-b04f-70bf9263d8d1-1&pdp_npi=4%40dis%21ILS%21368.56%21239.58%21%21%2196.07%2162.45%21%40211b815c17146664569388304e6a78%2112000033194823078%21sea%21IL%210%21AB&curPageLogUid=vl3GT8zZ4HtX&utparam-url=scene%3Asearch%7Cquery_from%3A"

# Get the price
price = get_price(URL)
if price is not None:
    print("Current price:", price)

    # Sending email notification if the price is below a certain threshold
    MY_EMAIL = 'mitaynewman@gmail.com'
    MY_PASSWORD = 'nitay2k1'
    BUY_PRICE_THRESHOLD = 100  # Set your desired threshold

    if price < BUY_PRICE_THRESHOLD:
        with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg=f'Subject: Price Drop Alert!\n\nThe price of the product has dropped below {BUY_PRICE_THRESHOLD}₪.\nCurrent Price: {price}₪.\n\nCheck it out here: {URL}'
            )
            print("Email notification sent!")
else:
    print("Price not available.")

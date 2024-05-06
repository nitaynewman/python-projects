import requests
from twilio.rest import Client
# can use whatkit insted of twilio


STOCK_NAME = 'TSLA'
COMPANY_NAME = 'Tesla Inc'
STOCK_ENDPOINT = 'https://www.alphavantage.co/query'
STOCK_API_KEY = 'A7XIIEJKEPMGRNBK'

NEWS_ENDPOINT = 'https://newsapi.org/v2/everything'
NEWS_API_KEY = 'f8de8e04f92a4c5d91a5c5cef35d55fa'

TWILIO_SID = 'TWILIO_SID'
TWILIO_TOKEN = 'TWILIO_TOKEN'

# ------------------------ STOCK API ------------------------ #
stock_params = {
  'function': 'TIME_SERIES_DAILY',
  'symbol': STOCK_NAME,
  'apikey': STOCK_API_KEY
}

# ------------------------ TODAYS STOCK DATA ------------------------ #
response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()['Time Series (Daily)']
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = float(yesterday_data['4. close'])
print(yesterday_closing_price)

# ------------------------ DAY BEFORE STOCK DATA ------------------------ #
day_before_data = data_list[1]
day_before_closing_price = float(day_before_data['4. close'])
print(day_before_closing_price)

# ------------------------ DIFFRENCE ------------------------ #
diffrence = yesterday_closing_price - day_before_closing_price
up_down = None
if diffrence > 0:
  up_down = '✔😊'
else:
  up_down = '😫❌'

# ------------------------ PERCENTAGE DIFFRENCE ------------------------ #
diff_percent = round((diffrence / yesterday_closing_price) * 100)
print(diff_percent)

if abs(diff_percent) > 5:
  news_params = {
    'apiKey': NEWS_API_KEY,
    'qInTitle': COMPANY_NAME,
  }
  news_responce = requests.get(NEWS_ENDPOINT, params=news_params)
  articles = news_responce.json()['articles']
  three_articles = articles[:3]
  print(three_articles)


# ------------------------ SMS FORMAT ----------------------- #
format_articale = [f"{STOCK_NAME}: {up_down} {diff_percent}% \nHeadline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]

# ------------------------ SMS SENDER ----------------------- #
client = Client(TWILIO_SID, TWILIO_TOKEN)
for article in format_articale:
  message = client.messages.create(
           body=article,
           from_='+15017122661',
           to='+15558675310'
       )



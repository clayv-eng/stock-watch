from stock_api import AVStockRequest
from stock import Stock
from sms_alert import Alert
import datetime as dt
import os

AV_API_KEY = os.environ.get("AV_API_KEY")
MY_NUMBER = os.environ.get("MY_NUMBER")
TODAY = dt.datetime.today().date()
YESTERDAY = TODAY - dt.timedelta(days=1)
CLOSE = "4. close"
COMPANY_NAME = "Tesla"
SYMBOL = "TSLA"
IND_SYMBOLS = {"UP": "🔺", "DOWN": "🔻"}


def get_price_movement(prev_day, curr_day):
    curr_day = float(curr_day)
    prev_day = float(prev_day)
    movement = (curr_day - prev_day) / curr_day * 100
    return round(movement, 4)


tsla = Stock(name=COMPANY_NAME, symbol=SYMBOL, key=AV_API_KEY)
tsla_today_close_price = tsla.get_day_data(day=str(YESTERDAY)).get(CLOSE)
tsla_yesterday_close_price = tsla.get_day_data(day=str(YESTERDAY - dt.timedelta(days=1))).get(CLOSE)
tsla_movement = get_price_movement(tsla_yesterday_close_price, tsla_today_close_price)

if tsla_movement > 0:
    arrow = IND_SYMBOLS.get("UP")
else:
    arrow = IND_SYMBOLS.get("DOWN")

articles = tsla.get_day_article()[:4]
article_list = [f"\nHeadline: {article.get('title')}\nBrief: {article.get('description')}" \
                f"\n{article.get('url')}" for article in articles]

print(tsla_today_close_price, tsla_yesterday_close_price)
for article in article_list:
    tsla_message = f"{SYMBOL} ${tsla_today_close_price} USD {arrow}{tsla_movement}%{article}"
    tsla_alert = Alert(receive_number=MY_NUMBER, message=tsla_message)
    tsla_alert.send_alert()
    print(tsla_message)

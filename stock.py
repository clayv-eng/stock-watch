from stock_api import AVStockRequest
import datetime as dt
import requests
from newsapi import NewsApiClient

TODAY = str(dt.datetime.today().date())


class Stock:
    def __init__(self, name: str, symbol: str, key: str):
        self.name = name
        self.symbol = symbol
        self.baseline_request = AVStockRequest(symbol=symbol, key=key)
        self.daily_adjusted_data = self.baseline_request.get_daily_adjusted_data()
        self.weekly_adjusted_data = self.baseline_request.get_weekly_adjusted_data()
        self.stock_news_client = NewsApiClient(api_key="8f6136e2191b420ab9a90b9c0cc37b42")
        # self.today_data = self.get_today_data()
        # self.yesterday_data = self.get_yesterday_data()
        # self.today_open_price = self.today_data["1. open"]
        # self.yesterday_open_price = self.yesterday_data["1. open"]
        # self.daily_price_movement = get_price_movement(prev_day=self.yesterday_open_price,
        #                                                curr_day=self.today_open_price
        #                                                )

    def get_day_data(self, day: str = TODAY):
        if day in self.daily_adjusted_data:
            data = self.daily_adjusted_data[day]
            return data
        elif day == str(dt.datetime.today().date()):
            return {"Market Status": "Still Open"}
        else:
            return {"Queried Date": "Out of Range"}

    def get_day_article(self, day: str = TODAY):
        article = self.stock_news_client.get_everything(qintitle=self.name, from_param=day, to=day, sort_by="relevancy")
        return article.get("articles")

    def get_headline(self, lang: str = "en", **kwargs):
        article = self.stock_news_client.get_top_headlines(qintitle=self.name,
                                                           language=lang,
                                                           category=kwargs.get("cat"),
                                                           country=kwargs.get("country")
                                                           )
        return article.get("articles")

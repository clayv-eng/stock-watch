import requests

REQUEST_FUNCTIONS = {"daily adjusted": "TIME_SERIES_DAILY_ADJUSTED",
                     "weekly adjusted": "TIME_SERIES_WEEKLY_ADJUSTED"
                     }


class AVStockRequest:
    def __init__(self, symbol: str, key: str):
        self.url = "https://www.alphavantage.co/query"
        self.symbol = symbol
        self.function_dict = REQUEST_FUNCTIONS
        self.key = key

    def get_daily_adjusted_data(self, **kwargs):
        parameters = {"function": self.function_dict.get("daily adjusted"),
                      "symbol": self.symbol,
                      "apikey": self.key,
                      "datatype": kwargs.get("datatype")
                      }
        data = requests.get(url=self.url, params=parameters).json()
        for key, value in data.items():
            if "Time Series" in key:
                parsed_data = value
                return parsed_data

    def get_weekly_adjusted_data(self, **kwargs):
        parameters = {"function": self.function_dict.get("weekly adjusted"),
                      "symbol": self.symbol,
                      "apikey": self.key,
                      "datatype": kwargs.get("datatype")
                      }
        data = requests.get(url=self.url, params=parameters).json()
        for key, value in data.items():
            if "Time Series" in key:
                parsed_data = value
                return parsed_data

import pandas as pd
import numpy as np
import datetime



class request():

    def __init__(self) -> None:
        self.df = pd.read_csv("Pandas\\Datasets\\earthquake.csv")
        self.df["date"] = pd.to_datetime(self.df["date"], format="%Y.%m.%d").dt.date
        self.df["md"] = pd.to_numeric(self.df["md"])

    def search_by_coutry(self, country):
        country = str.lower(country)
        return self.df[self.df["country"] == country]
    
    def search_by_city(self, city):
        city = str.lower(city)
        return self.df[self.df["city"] == city]

    #we will get date at string format, so we must convert it to date object
    def search_by_date(self, start_date, end_date):
        start_date = datetime.datetime.strptime(start_date, "%d.%m.%Y").date()
        end_date = datetime.datetime.strptime(end_date, "%d.%m.%Y").date()
        filtered_records = self.df[
            (self.df["date"] >= start_date) & (self.df["date"] <= end_date)
        ]

        return filtered_records
       
    def search_by_magnitude(self, start_value, end_value):
        start_value = float(start_value)
        end_value = float(end_value)
        filtered_records = self.df[
            (self.df["md"] >= start_value) & (self.df["md"] <= end_value)
        ]

        return filtered_records



req = request()
response = req.search_by_magnitude("3.0","7.5").sort_values("md")
print(response)
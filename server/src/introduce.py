from datetime import datetime
import pandas as pd

file_path = './raw_data/forex.csv'
raw_data = pd.read_csv(file_path)
print("load raw data successfully!")

def get_currency(slug, start_time, end_time):
    start_time = datetime.strptime(start_time, '%Y-%m-%d')
    end_time = datetime.strptime(end_time, '%Y-%m-%d')
    opens, highs, lows, closes, dates = [],[],[],[], []
    for slug_, open_, high, low, close, date in zip(raw_data['slug'], raw_data['open'],\
                                           raw_data['high'], raw_data['low'], raw_data['close'], raw_data['date']):
        if slug == slug_:
            datetime_date = datetime.strptime(date, '%Y-%m-%d')
            if start_time <= datetime_date and end_time >= datetime_date:
                opens.append(open_)
                highs.append(high)
                lows.append(low)
                closes.append(close)
                dates.append(date)
    return opens, highs, lows, closes, dates
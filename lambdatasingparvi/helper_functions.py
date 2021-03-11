
import pandas as pd
import numpy as np
# def null_count(df):
#     print(df.isnull().sum().sum())
from IPython.core.display import display

df = pd.read_csv('/Users/rob/G_Drive_sing.parvi/Colab_Notebooks/Unit-2-Linear-Models/Sprint_4_Build_Precipitation_Prediction/ForestCover.csv')

# null_count(test)


# def train_test_split(df, frac):
# #
# i = len(test.index)*0.2
# print(i)
#
# a, b = np.split(test, 2, axis=0)

df1 = pd.read_csv('/Users/rob/G_Drive_sing.parvi/Colab_Notebooks/Unit-2-Linear-Models/Sprint_4_Build_Precipitation_Prediction/prec_ps_wind_temp_data.csv')

dates = df1['date']

print(type(dates))

dates = pd.to_datetime(dates, infer_datetime_format=True)

print(dates)
def split_dates(date_series):
    month = date_series.dt.month
    day = date_series.dt.day
    year = date_series.dt.year
    frame = { 'month': month, 'day': day, 'year': year }
    output = pd.DataFrame(frame)
    print(output)



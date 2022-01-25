"""
Script written by pavithraes to ...

Caveats: (1) 
"""

import pandas as pd
import matplotlib as mlp
import matplotlib.pyplot as plt

from condastats.cli import overall

libraries = ['dask', 'distributed', 'numpy', 'pandas', 'airflow', 'vaex', 'ray', 'pyspark', 'modin']

start_month="2017-01"
end_month="2021-12"

raw_data = overall(libraries, start_month=start_month, end_month=end_month, monthly=True).reset_index(level=[0,1])
raw_data['time'] = pd.to_datetime(raw_data['time'])

data = pd.pivot_table(raw_data, values='counts', index='time', columns='pkg_name')

def change_per_year(m):
    month = data.iloc[lambda x: x.index.month == m]
    month.index = month.index.year

    df_roll = month.rolling(2).mean()
    df_perc = (month.diff().div(df_roll) * 100).iloc[1:].round(2).astype(str) + '%'

    final = month.astype(str) + " (" + df_perc + ")"
    final.drop(index=2017, inplace=True)
    return final

if __name__ == "__main__":
    m = int(input()) # Month as int. Example: for Jan, m = 1.
    change_per_year(12).to_html(f"files/conda-metrics-{m}-2022.html")
    print(f"'files/conda-metrics-{m}-2022.html' created successfully")

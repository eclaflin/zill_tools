import os
import pandas as pd

csv_filepath = os.path.join("tax_rates","ma_tax_rates.csv")

df_tax_rates = pd.read_csv(csv_filepath)

print(df_tax_rates.head())


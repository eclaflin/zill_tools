import os
import pandas as pd

csv_filepath = os.path.join("tax_rates","ma_tax_rates.csv")

df_tax_rates = pd.read_csv(csv_filepath)

#print(df_tax_rates.head())

def rate_pull(town):
    df_out = df_tax_rates.loc[
        (df_tax_rates['Municipality']==town) & (df_tax_rates['Fiscal Year']==2023)
        ]
    
    return df_out['Residential'].iloc[0].astype('float')
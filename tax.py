import os
import pandas as pd

csv_filepath = os.path.join("tax_rates","ma_tax_rates.csv")

df_tax_rates = pd.read_csv(csv_filepath)

#this is so gross but jp isn't a city so here we are
bos_zips = ['02101',
            '02102',
            '02103',
            '02104',
            '02105',
            '02106',
            '02107',
            '02108',
            '02109',
            '02110',
            '02111',
            '02112',
            '02113',
            '02114',
            '02115',
            '02116',
            '02117',
            '02118',
            '02119',
            '02120',
            '02121',
            '02122',
            '02123',
            '02124',
            '02125',
            '02126',
            '02127',
            '02128',
            '02129',
            '02130',
            '02131',
            '02132',
            '02133',
            '02134',
            '02135',
            '02136',
            '02137',
            '02163',
            '02199',
            '02203',
            '02205',
            '02208',
            '02209',
            '02210',
            '02215',
            '02222',
            '02228',
            '02283',
            '02284',
            '02455'
        ]

def rate_pull(zip, town):
    if zip in bos_zips:
        df_out = df_tax_rates.loc[
            (df_tax_rates['Municipality']=='Boston') & (df_tax_rates['Fiscal Year']==2023)
            ]
        
    else:
        df_out = df_tax_rates.loc[
            (df_tax_rates['Municipality']=='Boston') & (df_tax_rates['Fiscal Year']==2023)
            ]
    
    return df_out['Residential'].iloc[0].astype('float')
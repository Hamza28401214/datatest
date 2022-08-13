import pandas as pd
import sqlite3
from pathlib import Path
pat = str(Path(__file__).parent.parent)


def extract(pat):
    df = pd.read_excel(pat+'\\data//gdp_Tunisia.xlsx')
    return df


def transform(df):
    df = df.dropna() #removing nan values
    df2 = df.copy()
    df2['GDP_growth'] = df['GDP_growth'].apply(lambda x: round(x, 2)) #applying round
    df2['GDP'] = df['GDP'].apply(lambda x: round(x, 2))
    #feature engineering
    df2['positive_growing'] = df2['GDP_growth'].ge(0) #replacing positive gdp growth by True, false for opposite
    return df2


def load(df):
    try:
        con = sqlite3.connect(pat + '\\database//final_data.db')
        df.to_sql(con=con, name='tun_tab', if_exists='replace')
        con.close()
    except Exception as e:
        print(e)
        return False
    return True






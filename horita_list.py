import pandas as pd

df = pd.read_csv('taigigo.csv',header = None)

df2 = pd.DataFrame(index=[], columns = df.columns)

for index, rows in df.iterrows():
    series = pd.Series([rows[1], rows[0]], index = df2.columns )
    df2 = df2.append(series, ignore_index = True)

of_alltagigo = df_alltagigo.reset_index(drop=True)
print(df_alltagigo[:3])


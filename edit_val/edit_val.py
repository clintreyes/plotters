import pandas as pd

df = pd.read_csv('wave_bc.csv')

rows = df.shape[0]

for i in range(rows):
    if df['Hs'][i] == 0:
        df['Hs'][i] = 10

df.to_csv('edit_val_out.csv', index = False)

#a = df['Hs'].isnull().sum() #df[col].isnull().sum()

#df_mod = df.dropna() #df.fillna(" ") -> for fill
#c_m = df_mod['direction'].isnull().sum() -> print check


import pandas as pd

df = pd.read_csv('wave_bc.csv')

#df.shape
#df.isnull()

a = df.isnull().sum() #df[col].isnull().sum()
#c = df['direction'].isnull().sum() -> print check

df_mod = df.dropna() #df.fillna(" ") -> for fill
#c_m = df_mod['direction'].isnull().sum() -> print check

df_mod.to_csv('modified_wave_bc.csv', index = False)

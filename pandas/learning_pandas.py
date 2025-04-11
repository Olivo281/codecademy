import pandas as pd
csv_path = r'/home/richi/trade/data/historical/stocks/D/AAPL.csv'

#EX 1   
dataf = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'Banana': [7, 8, 9]},columns=['Banana','A', 'B'])
dataf.set_index('Banana', inplace=True)
print(dataf)

#EX 2

# df= pd.read_csv(csv_path)
# print(df)
# print(df.head())
# print(df.tail())
# print(df.info())

#Dataframe
df = pd.DataFrame([
  ['January', 100, 100, 23, 100],
  ['February', 51, 45, 145, 45],
  ['March', 81, 96, 65, 96],
  ['April', 80, 80, 54, 180],
  ['May', 51, 54, 54, 154],
  ['June', 112, 109, 79, 129]],
  columns=['month', 'clinic_east',
           'clinic_north', 'clinic_south',
           'clinic_west']
)
#more examples
filtered_rows = df[df['clinic_east'].isin([100, 51])]

print(filtered_rows)

# df2 = df.loc[[1, 3, 5]]

# # print(df2)

# df3 = df2.reset_index()

# print(df3)

# df2.reset_index(inplace = True, drop = True)

# print(df2)

                                                            
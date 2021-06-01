import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('cities/results_philly.csv')
df1 = pd.read_csv('cities/results.csv')

merged_file = pd.merge(df,df1, left_on='year', right_on='year', how='left')

merged_file.to_csv('merged_file.csv', index=False)

df_merged = pd.read_csv('merged_file.csv')


df = df_merged[['year','city_x','city_y','avg_temp_x','avg_temp_y']]
#df = df.fillna(0)

#df1 = df1[['year','city','avg_temp']]
#df1 = df.fillna(0)

#print(df.head(15))
#print(df1.head(15))
#
# df_join = df.merge(right=df1, left_on=df.columns.tolist(),
#                    right_on= df1.columns.tolist(),
#                    how='outer')

#df_join.to_csv('new_file.csv', index = False)




df_merged['7-day MA'] = df_merged.avg_temp_y.rolling(window=7).mean()
#df1['7-day MA'] = df.avg_temp.rolling(window=7).mean()

#print(df.head(15))

plt.figure(figsize=(12, 8))
plt.title('Average Weather 1743 - 2013 (7- days MA)')

plt.plot( df_merged['year'], df_merged['city_x'],df_merged['avg_temp_x'],df_merged['city_y'],df_merged['avg_temp_y'],'b.-')
# plt.plot( df1['year'], df1['avg_temp'],'r.-')


plt.xlabel('Year')
plt.ylabel('Temperature(C)')
plt.xticks(df_merged.year[::15])
# plt.xticks(df1.year[::15])

#plt.yticks(df.avg_temp[::1/5])

plt.legend()
plt.show()



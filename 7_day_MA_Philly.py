import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('cities/results_philly.csv')

df = df.fillna(0)

df = df[['year','city','avg_temp']]

#print(df.head(15))

df['7-day MA'] = df.avg_temp.rolling(window=7).mean()

#print(df.head(15))

plt.figure(figsize=(12, 8))
plt.title('Philadelphia Temperature Change 1743 - 2013 (7- days MA)')

plt.plot( df['year'],df['avg_temp'],'b.-')


plt.xlabel('Year')
plt.ylabel('Temperature(C)')
plt.xticks(df.year[::15])
# plt.xticks(df1.year[::15])

#plt.yticks(df.avg_temp[::1/5])

plt.legend()
plt.show()



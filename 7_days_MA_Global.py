import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('cities/results_philly.csv')
df_global = pd.read_csv('cities/global_data.csv')

#df = df.fillna(0)


df = df[['year','city','avg_temp']]
df_global = df_global[['year','avg_temp']]

#print(df.head(15))

df['7-year MA'] = df.avg_temp.rolling(window=7).mean()
df_global['7-year MA Globe'] = df_global.avg_temp.rolling(window=7).mean()

#print(df.head(15))

df.set_index('year')['7-year MA'].plot()
df_global.set_index('year')['7-year MA Globe'].plot()

#plt.figure(figsize=(12, 8))
fig, ax = plt.subplots(figsize=(14, 8))

plt.title('Temperature Change 1743 - 2013 (7-year MA)')

#plt.plot( df['year'], df['avg_temp'],'b.-')
df.set_index('year')['7-year MA'].plot(ax=ax,
                                        color='r',
                                        label="Philadephia 7 Year Moving Average")

df_global.set_index('year')['7-year MA Globe'].plot(ax=ax,
                                                    color='b',
                                                    label="Global 7 Year Moving Average")

# plt.xlabel('Year')
# plt.ylabel('Temperature(C)')
plt.xticks(df.year[::15])
# plt.xticks(df1.year[::15])

#plt.yticks(df.avg_temp[::1/5])

plt.legend()
plt.show()



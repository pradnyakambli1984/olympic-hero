# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
path

#Code starts here
data=pd.read_csv(path)
data.rename(columns={'Total':'Total_Medals'},inplace=True)
data.head(10)


# --------------
#Code starts here
data['Better_Event'] = np.where(data['Total_Summer']>data['Total_Winter'],'Summer',np.where(data['Total_Summer']<data['Total_Winter'],'Winter','Both'))

better_event=data['Better_Event'].value_counts().idxmax()


# --------------
#Code starts here
top_countries = data[['Country_Name','Total_Summer','Total_Winter','Total_Medals']]

top_countries.drop(top_countries.shape[0]-1,axis=0,inplace=True)

def top_ten(df,name):
    country_list = []
    country_list = list(df.nlargest(10,name)['Country_Name'].values)
    return country_list

top_10_summer = top_ten(top_countries,'Total_Summer')
top_10_winter = top_ten(top_countries,'Total_Winter')
top_10 = top_ten(top_countries,'Total_Medals')

common = [i for i in top_10_summer if i in top_10_winter and i in top_10]
print(common)



# --------------
#Code starts here
summer_df=data[data['Country_Name'].isin(top_10_summer)]

winter_df=data[data['Country_Name'].isin(top_10_winter)]

top_df=data[data['Country_Name'].isin(top_10)]

print(summer_df.columns)

plt.bar(summer_df['Country_Name'],summer_df['Total_Summer'])
plt.bar(winter_df['Country_Name'],winter_df['Total_Winter'])
plt.bar(top_df['Country_Name'],top_df['Total_Winter'])


# --------------
#Code starts here
summer_df['Golden_Ratio']=summer_df['Gold_Summer']/summer_df['Total_Summer']
summer_max_ratio=summer_df['Golden_Ratio'].max()
summer_country_gold =  summer_df.ix[summer_df['Golden_Ratio'].idxmax(),'Country_Name']


winter_df['Golden_Ratio']=winter_df['Gold_Winter']/winter_df['Total_Winter']
winter_max_ratio=winter_df['Golden_Ratio'].max()
winter_country_gold =  winter_df.ix[winter_df['Golden_Ratio'].idxmax(),'Country_Name']

top_df['Golden_Ratio'] = top_df['Gold_Total']/top_df['Total_Medals']
top_max_ratio = top_df['Golden_Ratio'].max()
top_country_gold = top_df.ix[top_df['Golden_Ratio'].idxmax(),'Country_Name']


# --------------
#Code starts here
data_1 = data[:-1]
data_1['Total_Points'] = data_1['Gold_Total']*3 + data_1['Silver_Total']*2 + data_1['Bronze_Total']

most_points = data_1['Total_Points'].max()
best_country = data_1.ix[ data_1['Total_Points'].idxmax(),'Country_Name']


# --------------
#Code starts here
best = data[data['Country_Name']==best_country][['Gold_Total','Silver_Total','Bronze_Total']]

best.plot(kind='bar')

plt.xlabel('United States')
plt.ylabel('Medals Tally')
plt.xticks(rotation=45)



import pandas as pd

# importing csv file in a dataframe
df = pd.read_csv('crop_yield.csv')

#--------- Basic Checks -------- 
#Check the data first in the csv file
print(df.head(5))

# Check the basic statistics like count, mean for the numerical columns
print(df.describe())

#Check the summary like datatype, total number of rows and if there is any null value in dataset
print(df.info())

#We can also check null value for any particular column like Crop
print(df.Crop.isnull().sum())

# Check which Crop is produced how much
df_Crop_Count = df.groupby('Crop').Crop.count()

#------ Data Analysis -------
#Sorting it by descending order to check which is produced most to less
print(df.groupby('Crop').Crop.count().sort_values(ascending=False))

#Checking the seasonal Crop growth
Seasonal_Crop_Growth = df.groupby(['Season','Crop']).Crop.count()
Seasonal_Crop_Growth = Seasonal_Crop_Growth.reset_index(name='CNT')
print(Seasonal_Crop_Growth.Season.unique()) # Trailing Spaces in Season name

Seasonal_Crop_Growth['Season'] = Seasonal_Crop_Growth['Season'].apply(lambda x: ' '.join(x.split()))

print(Seasonal_Crop_Growth.Season.unique()) # Removed the trailing spaces

for i in Seasonal_Crop_Growth.Season.unique():
    print(Seasonal_Crop_Growth[Seasonal_Crop_Growth['Season']==i].sort_values(by='CNT',ascending=False).iloc[0])

#Checking which Crop yielded most the last year
Max_Year = df.Crop_Year.max()
Latest_Crop_df = df[df['Crop_Year']==Max_Year]
Crop_Seasonwise_Latest_df = Latest_Crop_df.groupby(['Crop','Season']).Yield.mean().sort_values(ascending=False)
Crop_Seasonwise_Latest_df = Crop_Seasonwise_Latest_df.reset_index(name='CNT')

for i in Latest_Crop_df.Season.unique():
    print(Crop_Seasonwise_Latest_df[Crop_Seasonwise_Latest_df['Season']==i].iloc[0])

import pandas as pd

purchase = pd.read_csv('amazon-purchases.csv')
survey = pd.read_csv('survey.csv')

# left join on survey ID
df = purchase.merge(survey, how='left', on='Survey ResponseID')

#shortening column names, removing dashes and spaces
df.columns = ['OrderDate', 'PurchasePricePerUnit', 'Quantity',
       'ShippingAddressState', 'Title', 'ASIN/ISBN',
       'Category', 'SurveyResponseID', 'age', 'hispanic',
       'race', 'education', 'income', 'gender',
       'sexualorientation', 'state', 'amazonhowmany',
       'amazonusehhsize', 'amazonusehowoft',
       'cigarettes', 'marijuana',
       'alcohol', 'diabetes',
       'wheelchair', 'lifechanges', 'sellYOURdata',
       'sellconsumerdata', 'smallbizuse', 'censususe',
       'researchsociety']

# Creating dataframe with both videogame categories
df1 = df.loc[df['Category']=='DOWNLOADABLE_VIDEO_GAME']
df2 = df.loc[df['Category']== 'PHYSICAL_VIDEO_GAME_SOFTWARE']

df_games = pd.concat([df1, df2])
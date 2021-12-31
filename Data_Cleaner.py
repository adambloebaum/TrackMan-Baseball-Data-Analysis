#import modules
import pandas as pd

#read in csv as dataframe
#include filename
df=pd.read_csv('FILENAME.csv', index_col=False)

#select columns
df=df[['PitchNo','Pitcher','TaggedPitchType','RelSpeed','SpinRate','Tilt','InducedVertBreak',
       'HorzBreak','PitchCall']]

#create pitch count column
pitch_count = df['PitchNo'].max()

#round values to 1 decimal
df=df.round(decimals=1)

#group data into new datframe and take mean of pitch type
final_report=df.groupby(['Pitcher','TaggedPitchType']).mean()

#drop column
final_report=final_report.drop('PitchNo', axis=1)

#round values to 1 decimal
final_report=final_report.round(decimals=1)

#save as new csv
#include full directory path
final_report.to_csv(r'C:\PATH.csv')

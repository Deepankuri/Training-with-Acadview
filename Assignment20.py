#Question1
import pandas as pd
data = {'name':['iusub'],'age':['20'],'email id':['kjhbg@mail.com'],'phone no':['687163564']}
frame1 = pd.DataFrame(data)
frame1.loc[1] = ['kaudiyt', '14', 'liastvo@gmail.coom','2687']
print(frame1)

#Question2
import pandas as pd
frame2 = pd.read_csv('weather.csv')
print('first 5 rows', frame2.head(5))
print('first 10 rows', frame2.head(10))
print('basic stats : min and max temp', frame2['MinTemp'].describe(), frame2['MaxTemp'].describe())
print('extracting second column')
print('sum', frame2.iloc[:,2].sum())
print('min', frame2.iloc[:,2].sum())
print('max', frame2.iloc[:,2].sum())
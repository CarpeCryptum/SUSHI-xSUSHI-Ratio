import pandas as pd
import matplotlib.pyplot as plt
import requests
import json
import datetime

url='https://api.thegraph.com/subgraphs/name/sushi-labs/xsushi'

query='''{
  weekSnapshots(first:500){
    date
    sushiXsushiRatio
  }
}'''

page=requests.post(url, json={'query': query})
data=json.loads(page.text)
data_list=data['data']['weekSnapshots']
period=[]
ratio=[]
for i in data_list:
    period.append(i['date'])
    ratio.append(i['sushiXsushiRatio'])

date=[]
for i in period:
    date.append(datetime.datetime.fromtimestamp(i).strftime('%d-%m-%y'))

df=pd.DataFrame(date, columns=['date'])
df['ratio']=(ratio)
df['ratio']=df['ratio'].astype(float)
df.to_csv('xSUSHIratio.csv')
df['ratio']=df['ratio'].round(3)
df.plot(x ='date', y='ratio', kind = 'line')
plt.show()

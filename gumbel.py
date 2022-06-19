import pandas as pd
import math 
import matplotlib.pyplot as plt

data=pd.read_csv('mangalsen.csv')

data=data.sort_values(by="Extr",ascending= False)

data['rank']=data['Extr'].rank(method='first',ascending= False)
n=(data.shape[0])
data['Ret_period']=(n+1)/data['rank']
x_avg=data['Extr'].mean()
s=data['Extr'].std()

# for n=30
sn=1.1124
yn=0.5362
return_periods=[5,10,20,33,50,100,200,500]
k_list=[]
yt_list=[]
for x in return_periods:
    yt=-(0.834+2.303*math.log(math.log(x/(x-1),10),10))
    k=(yt-yn)/sn
    k_list.append(k)
    yt_list.append(yt)

dict={'return_period': return_periods,'k' :k_list,'yt': yt_list}
final=pd.DataFrame(dict)
final["Pred_flow"]=x_avg+final['k']*s
print(final.head(10))


plt.plot(final['yt'],final['Pred_flow'])
plt.xlabel("Return periods(yrs)")
plt.ylabel("Flood discharge(m^3")
# secax=plt.secondary_xaxis('top',final['Pred_flow'])
plt.show()


from scipy import stats
r=stats.pearsonr(final['return_period'],final['Pred_flow'])
print(r[0])
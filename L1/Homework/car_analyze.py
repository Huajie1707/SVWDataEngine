# 对汽车投诉信息进行分析
import pandas as pd
import numpy as np

print('Step1')
result = pd.read_csv("..\car_data_analyze\car_complain.csv")
print('mount =',len(result))

print('Step2')
result_index = result.problem.str.split(',', expand=True).stack().to_frame()
result_index = result_index.reset_index(level=1, drop=True).rename(columns={0:'problem'})
result = result.drop('problem', 1).join(result_index)
result = result[~result['problem'].isin([''])]

print('Step3')

rs1 = result.groupby('brand').count().sort_values('id', ascending=False)
#rss = rs1['brand']
print(rs1.loc[:,['id']].rename(columns={'id':'result'}))
rs2 = result.groupby('car_model').count().sort_values('id', ascending=False)
print(print(rs2.loc[:,['id']].rename(columns={'id':'result'})))
#rs3 = result.groupby(['brand','car_model']).count()
#print(rs3)
rs4 = result.groupby(['brand','car_model']).count().groupby('brand', group_keys=False).agg([np.mean])#.sort_values('id', axis=1, ascending=False)
print(rs4.loc[:,['id']])


# 将genres进行one-hot编码（离散特征有多少取值，就用多少维来表示这个特征）
#result = result.drop('problem', 1).join(result.problem.str.get_dummies(','))

#result = result.drop(['problem'], axis=1).join(result['problem'].str.split(',', expand=True).stack().reset_index(level=1, drop=True).rename('problem_new'))

#result[['id']].join(result_index)

#tags = result.columns[7:]
#print(tags)

#df= result.groupby(['brand'])['id'].agg(['count'])
#df2= result.groupby(['brand'])[tags].agg(['sum'])
#df2 = df.merge(df2, left_index=True, right_index=True, how='left')
# 通过reset_index将DataFrameGroupBy => DataFrame
#df2.reset_index(inplace=True)
#df2.to_csv('temp.csv')
#df2= df2.sort_values('count', ascending=False)
#print(df2)
#print(df2.columns)
#df2.to_csv('temp.csv', index=False)
#query = ('A11', 'sum')
#print(df2.sort_values(query, ascending=False))

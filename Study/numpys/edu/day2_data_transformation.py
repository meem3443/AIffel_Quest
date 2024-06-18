#!/usr/bin/env python
# coding: utf-8

# # Data merge(데이터 병합)

# In[83]:


import pandas as pd
import numpy as np


# In[84]:


df_a = pd.DataFrame({'key': ['a','b','c','d','e'], 'num_a': [1,2,3,4,5]})
df_b = pd.DataFrame({'key': ['a','b','d','f','g'], 'num_b': [11,15,35,45,55]})
df_c = pd.DataFrame({'key': ['f','g','h','i','j'], 'num_a': [6,7,8,9,0]})


# In[85]:


df_a


# In[86]:


df_b


# In[87]:


df_c


# In[88]:


pd.concat([df_a, df_b])


# In[89]:


pd.concat([df_a, df_c])


# In[90]:


pd.concat([df_a, df_b, df_c])


# In[91]:


pd.concat([df_a, df_b, df_c], axis = 1)


# In[92]:


df_a.merge(df_b, how = 'inner')


# In[93]:


df_a.merge(df_b, how = 'outer')


# In[94]:


df_a.merge(df_b, how = 'left')


# In[95]:


df_a.merge(df_b, how = 'right')


# In[96]:


df_a.merge(df_b, on = 'key' ,how = 'right')


# In[97]:


df_a = pd.DataFrame({'key': ['a','b','c','d','e'], 'id': ['q','w','e','r','t'] ,'num_a': [1,2,3,4,5]})
df_b = pd.DataFrame({'key': ['a','b','d','f','g'], 'id': ['r','t','z','x','y'] ,'num_b': [11,15,35,45,55]})


# In[98]:


df_a


# In[99]:


df_b


# In[100]:


df_a.merge(df_b, on = 'key')


# In[101]:


df_a.merge(df_b, on = 'id')


# In[102]:


df_a.merge(df_b, on = 'id', how = 'left')


# In[103]:


df_a = pd.DataFrame({'key': ['a','b','c','d','e'],'num_a': [1,2,3,4,5]})
df_b = pd.DataFrame({'id': ['a','b','d','f','g'],'num_b': [11,15,35,45,55]})


# In[104]:


df_a.merge(df_b, left_on = 'key', right_on = 'id', how = 'outer')


# In[105]:


df_a


# In[106]:


df_b


# In[107]:


df_a = pd.DataFrame({'key': ['a','b','c','d','e'],'num_a': [1,2,3,4,5]})
df_b = pd.DataFrame({'key': ['a','b','d','f','g'],'num_b': [11,15,35,45,55]})


# In[108]:


df_a.join(df_b, lsuffix = '_a', rsuffix = '_b')


# In[109]:


df_a = df_a.set_index('key')
df_b = df_b.set_index('key')


# In[110]:


df_a


# In[111]:


df_b


# In[112]:


df_a.join(df_b, how = 'outer')


# In[113]:


df_a.join(df_b, how = 'inner')


# In[114]:


salary_1 = pd.read_csv('salary_1.csv')
salary_2 = pd.read_csv('salary_2.csv')


# In[115]:


salary_1.head()


# In[116]:


salary_2.head()


# In[117]:


salary_df = pd.concat([salary_1, salary_2])


# In[118]:


salary_df.loc[0]


# In[119]:


salary_df.reset_index(drop = True, inplace = True)


# In[120]:


salary_df


# In[121]:


cpi = pd.read_csv('cpi.csv')


# In[122]:


cpi.head()


# In[123]:


salary_df['Country'].unique()


# In[124]:


cpi['Country'].unique()


# In[125]:


cpi['Country'] = cpi['Country'].replace({'United States': 'USA', 'United Kingdom': 'UK'})


# In[126]:


salary_df = salary_df.merge(cpi, on = 'Country', how = 'left')


# In[127]:


salary_df.head()


# In[128]:


salary_df.drop(['Reference','Previous','Units','Frequency'], axis = 1, inplace = True)


# In[129]:


salary_df.head()


# In[130]:


salary_df = salary_df.rename({'Last': 'CPI'}, axis = 1)


# In[131]:


salary_df.head()


# # 개요, 결측치&이상치(Missing Value & Outlier), 집계 및 그룹화(Aggregation and Group by), 피벗테이블(Pivot)

# In[132]:


salary_df.info()


# In[133]:


salary_df['CPI'] = pd.to_numeric(salary_df['CPI'])


# In[134]:


salary_df.describe()


# In[135]:


salary_df.isna().sum()


# In[136]:


salary_df.isna().mean()


# In[137]:


salary_df[salary_df['Age'].isna()]


# In[138]:


salary_df = salary_df.dropna()


# In[139]:


salary_df = salary_df[salary_df['Years of Experience'] != -1]


# In[140]:


salary_df['Years of Experience'].sort_values()


# In[141]:


salary_df[salary_df['Years of Experience'] == 82]


# In[142]:


salary_df = salary_df[~(salary_df['Years of Experience'] > salary_df['Age'] - 18)]


# In[143]:


salary_df.describe()


# In[144]:


salary_df[salary_df['Years of Experience']  == 0]


# In[145]:


salary_df.head()


# In[146]:


salary_df[salary_df['Gender'] == "Male"]['Salary'].mean()


# In[147]:


salary_df[salary_df['Gender'] == "Female"]['Salary'].mean()


# In[148]:


salary_df.groupby('Gender').mean()


# In[149]:


salary_df.groupby('Gender').max()


# In[150]:


salary_df.groupby('Gender')['Salary'].mean()


# In[151]:


salary_df.groupby('Gender')['Salary'].sum()


# In[152]:


salary_df.groupby('Gender')['Salary'].median()


# In[153]:


salary_df.groupby('Gender')['Salary'].std()


# In[154]:


salary_df.groupby(['Gender','Country'])['Salary'].mean()


# In[155]:


salary_df.groupby('Gender')['Salary'].agg(['sum','mean'])


# In[156]:


salary_df.groupby(['Gender','Country'])['Salary'].mean().reset_index()


# In[157]:


pd.pivot_table(salary_df, index = 'Gender', columns = 'Country', values = 'Salary')


# In[158]:


pd.pivot_table(salary_df, index = 'Gender', columns = 'Country', values = 'Salary', aggfunc = 'mean')


# In[159]:


pd.pivot_table(salary_df, index = 'Gender', columns = 'Country', values = 'Salary', aggfunc = np.mean)


# In[160]:


pd.pivot_table(salary_df, index = 'Gender', columns = 'Country', values = 'Salary', aggfunc = 'sum')


# In[161]:


pd.pivot_table(salary_df, index = ['Gender','Race'], columns = 'Country', values = 'Salary', aggfunc = 'sum')


# In[162]:


sales_df = pd.DataFrame({'company': ['a','a','a','a','b','b','b','b'],
             'quarter': ['q1','q2','q3','q4','q1','q2','q3','q4'],
             'sales': [111,222,333,444,555,666,777,888]})


# In[163]:


sales_df


# In[164]:


sales_temp = pd.pivot(sales_df, index = 'company', columns = 'quarter', values = 'sales')


# In[165]:


sales_temp.columns = sales_temp.columns.rename('')


# In[166]:


new_sales_df = sales_temp.reset_index()


# In[167]:


new_sales_df


# In[168]:


pd.melt(new_sales_df, id_vars = 'company', value_vars = ['q1','q2','q3','q4'], var_name ='quarter' ,value_name = 'sales').sort_values('company')


# # 로그(Log), 원-핫 인코딩 (One hot encoding)

# In[169]:


price_df = pd.DataFrame({'level':[1,2,3,4,5,6,7],
             'price': [1,10,100,1000,10000,100000, 1000000]})


# In[170]:


price_df


# In[171]:


import seaborn as sns


# In[173]:


sns.scatterplot(x = price_df['level'], y = np.log(price_df['price']))


# In[174]:


np.log(55)


# In[175]:


np.exp(4.007333185232471)


# In[179]:


salary_df.head()


# In[177]:


pd.set_option('display.max_columns', 50)


# In[178]:


pd.get_dummies(salary_df, columns = ['Gender','Country','Race','Job Title'], drop_first = True)


# # 스케일링 (Scaling)

# In[180]:


salary_df[['Gender','Country','Race','Job Title']].nunique()


# In[181]:


salary_df['Job Title'].value_counts().tail(20)


# In[ ]:


salary_df['Job Title'].unique()


# In[182]:


job = pd.read_csv('job.csv')


# In[183]:


salary_df = salary_df.merge(job, on = 'Job Title', how = 'left')


# In[184]:


salary_df.drop('Job Title', axis = 1, inplace = True)


# In[185]:


salary_df.head()


# In[186]:


salary_df['Jobs'].value_counts()


# In[187]:


salary_df.head()


# In[188]:


salary_df = pd.get_dummies(salary_df, columns = ['Gender','Country','Race','Jobs'], drop_first = True)


# In[189]:


salary_df['Age'].mean()


# In[190]:


salary_df['Age'].std()


# In[191]:


(salary_df['Age'] - salary_df['Age'].mean()) / salary_df['Age'].std()


# In[192]:


salary_df['Age'].quantile(0.75)


# In[193]:


(salary_df['Age'] - salary_df['Age'].quantile(0.5)) / (salary_df['Age'].quantile(0.75) - salary_df['Age'].quantile(0.25))


# In[194]:


salary_df['Age'].max()


# In[195]:


(salary_df['Age'] - salary_df['Age'].min()) / (salary_df['Age'].max() - salary_df['Age'].min())


# In[196]:


salary_df.head()


# In[200]:


from sklearn.preprocessing import StandardScaler, RobustScaler, MinMaxScaler


# In[201]:


ss = StandardScaler()
rs = RobustScaler()
mm = MinMaxScaler()


# In[202]:


ss.fit(salary_df)


# In[203]:


salary_df.columns


# In[204]:


ss_df = pd.DataFrame(ss.transform(salary_df), columns = salary_df.columns)


# In[205]:


rs.fit(salary_df)


# In[206]:


rs_df = pd.DataFrame(rs.transform(salary_df), columns = salary_df.columns)


# In[207]:


mm.fit(salary_df)


# In[208]:


mm_df = pd.DataFrame(mm.transform(salary_df), columns = salary_df.columns)


# In[210]:


ss_df.head()


# In[211]:


rs_df.head()


# In[212]:


mm_df.head()


# In[213]:


salary_df.head()


# In[214]:


ss_df.describe()


# In[215]:


round(3.406858e-17, 10)


# In[216]:


6674.000e+03


# In[217]:


1.000075e+00


# In[218]:


3.738204e+00


# In[219]:


-1.660937e+00


# In[220]:


rs_df.describe()


# In[221]:


mm_df.describe()


# In[222]:


ss.fit_transform(salary_df)


# #주성분 분석 (PCA), 복습 (Recap)

# In[223]:


from sklearn.decomposition import PCA


# In[224]:


pca = PCA()


# In[225]:


pca.fit(salary_df)


# In[226]:


salary_df


# In[227]:


pd.DataFrame(pca.transform(salary_df))


# In[228]:


pca = PCA(2)


# In[229]:


pd.DataFrame(pca.fit_transform(salary_df), columns = ['PC1','PC2'])


# In[230]:


(pca.explained_variance_ratio_).sum()


# In[231]:


salary_df.corr()


# In[ ]:





















'''
index title country
0 skoda	Czech Republic
1	vauxhall	United Kingdom
2	hyundai	South Korea
3	mini	United Kingdom
4	ford	United States
5	volvo	Sweden
6	peugeot	France
7	bmw	Germany
8	citroen	France
9	mercedes-benz	Germany
10	mazda	Japan
11	 saab	Sweden
12	volkswagen	Germany
13	honda	Japan
14	mg	United Kingdom
15	toyota	Japan
16	seat	Spain
17	nissan	Japan
18	alfa	Italy
19	renault	France
20	kia	South Korea
21	proton	Malaysia
22	fiat	Italy
23	audi	Germany
24	mitsubishi	Japan
25	lexus	Japan
26	land	United Kingdom
27	chevrolet	United States
28	suzuki	Japan
29	dacia	Romania
30	daihatsu	Japan
31	jeep	United States
32	jaguar	United Kingdom
33	chrysler	United States
34	rover	United Kingdom
35	ds	France
36	daewoo	South Korea
37	dodge	United States
38	porsche	Germany
39	subaru	Japan
40	infiniti	Japan
41	abarth	Italy
42	smart	Germany
43	marcos	United Kingdom
44	maserati	Italy
45	ssangyong	South Korea
46	lagonda	United Kingdom
47	isuzu	Japan


이렇게 데이터가 존재하는데
다른 데이터에서

'''
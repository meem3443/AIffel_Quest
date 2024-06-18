#!/usr/bin/env python
# coding: utf-8

# In[106]:


#데이터 가져오기
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
get_ipython().run_line_magic('matplotlib', 'inline')
get_ipython().run_line_magic('config', "InlineBackend.figure_format = 'retina'")

csv_path = os.getenv("HOME") +"/aiffel/pokemon_eda/data/Pokemon.csv"
original_data = pd.read_csv(csv_path) #원본 데이터 가져오기


# In[107]:


#원본 데이터를 가져오고 건들이지 않기 위해서 pokemon이라는 변수에 복사합니다.
pokemon = original_data.copy() #
print(pokemon.shape)
pokemon.head()


# In[108]:


#데이터의 결측치를 확인합니다.
pokemon.isnull().sum()


# In[109]:


legendary = pokemon[pokemon["Legendary"] == True].reset_index(drop=True)
ordinary = pokemon[pokemon["Legendary"] == False].reset_index(drop=True)


# In[110]:


#정보확인
pokemon.columns

#결과확인후 보니 타입을 두개씩 가지고있는 포켓몬도 있으나 한개만 가지는 포켓몬 있다는 것을 알 수 있었습니다.


# In[111]:


#Type1,2에는 어떤것이 있는지 확인합니다. 먼저 둘이 동일한 값을 가지고 있는지 확인합니다.
set(pokemon["Type 2"]) - set(pokemon["Type 1"]) 
set(pokemon["Type 2"]).difference(set(pokemon["Type 1"]))

#{nan}이 나왔으니 둘은 동일한 값을 가지고있습니다.
types = list(set(pokemon["Type 1"])) #Type 2로 동일한 결과를 보여줍니다.


# In[112]:


#포켓몬의 이름길이가 10자 이상인 포켓몬을 알아냅니다.
#이름이 10자이상이라면 long_name에 bool 형태로 값을 추가합니다.
pokemon["name_count"] = pokemon["Name"].apply(lambda i: len(i))
pokemon["long_name"] = pokemon["name_count"] >= 10
pokemon.head()


# In[113]:


#포켓몬의 이름의 띄어쓰기를 제거합니다.
pokemon["Name_nospace"] = pokemon["Name"].apply(lambda i: i.replace(" ", ""))
pokemon.tail()


# In[114]:


#포켓몬의 이름이 알파벳인지 확인합니다.
pokemon["name_isalpha"] = pokemon["Name_nospace"].apply(lambda i: i.isalpha())
pokemon.head()


# In[115]:


#포켓몬의 이름중 알파벳으로 구성되어있지 않는 타겟을 찾아냅니다.
print(pokemon[pokemon["name_isalpha"] == False].shape)
pokemon[pokemon["name_isalpha"] == False]


# In[116]:


#값이 많지 않으므로 수동으로 전부 바꿔줍니다.
pokemon = pokemon.replace(to_replace="Nidoran♀", value="Nidoran X")
pokemon = pokemon.replace(to_replace="Nidoran♂", value="Nidoran Y")
pokemon = pokemon.replace(to_replace="Farfetch'd", value="Farfetchd")
pokemon = pokemon.replace(to_replace="Mr. Mime", value="Mr Mime")
pokemon = pokemon.replace(to_replace="Porygon2", value="Porygon Two")
pokemon = pokemon.replace(to_replace="Ho-oh", value="Ho Oh")
pokemon = pokemon.replace(to_replace="Mime Jr.", value="Mime Jr")
pokemon = pokemon.replace(to_replace="Porygon-Z", value="Porygon Z")
pokemon = pokemon.replace(to_replace="Zygarde50% Forme", value="Zygarde Forme")

pokemon.loc[[34, 37, 90, 131, 252, 270, 487, 525, 794]]


# In[130]:


# 해당의 이름을 띄어쓰기로 나눈뒤 토큰화합니다.
import re
from collections import Counter

def tokenize(name):
    tokens = []
    name_split = name.split(" ")
    for part_name in name_split:
        a = re.findall('[A-Z][a-z]*', part_name)
        tokens.extend(a)
        
    return np.array(tokens)


all_tokens = list(legendary["Name"].apply(tokenize).values) #이름의 토큰화를 진행하였습니다. 이제 쉽게 이름의 패턴을 찾아낼 수 있습니다.
token_set = []
for token in all_tokens:
    token_set.extend(token)

most_common = Counter(token_set).most_common(10) # 몇개만 간추려 가장 많이 나온것을 순서대로 확인합니다.

for token, _ in most_common:
    # pokemon[token] = ... 형식으로 사용하면 뒤에서 warning이 발생합니다 
    pokemon[f"{token}"] = pokemon["Name"].str.contains(token) #해당값을 column에 추가합니다.
    
    


# In[131]:


#원 핫 인코딩을 진행합니다.
for t in types:
    pokemon[t] = (pokemon["Type 1"] == t) | (pokemon["Type 2"] == t)
    
pokemon[[["Type 1", "Type 2"] + types][0]].head()

pokemon.columns



# #### basline 사용 (No data annotation)

# In[132]:


#### 데이터처리

from sklearn.model_selection import train_test_split

features = ['Total', 'HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed', 'Generation'] #이중에서는 str 타입은 모두 제외합니다. (baseline은 str은 처리하지 않습니다.)
target = 'Legendary' #모델의 목적은 전설/일반 을 구분하는 것입니다.

x = original_data[features] 
y = original_data[target]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=15)


# #### 의사 결정 트리 사용

# from sklearn.tree import DecisionTreeClassifier
# model = DecisionTreeClassifier(random_state=25)
# 
# model.fit(x_train, y_train) #학습시작!
# y_pred = model.predict(x_test) #학습후 테스트 데이터로 성능 검증

# #정확도 판단

# In[133]:


from sklearn.metrics import confusion_matrix
result = confusion_matrix(y_test, y_pred)
print(f'TN: {result[0][0]} FR: {result[0][1]} FN: {result[1][0]} TP: {result[1][1]}')
print(f'정확도(TN + TP / Total) : {(result[0][0] + result[1][1])/ len(x_test) * 100}%')


# In[134]:


from sklearn.metrics import classification_report
recall = classification_report(y_test, y_pred)
print(recall)


# #### basline 사용 (data annotation)

# In[138]:


#pokemon.columns을 통해 호출했을때 필요없는 열은 다음과 같다.
# (#,Name,name_nospace,name_isalpha,Type 1, Type 2)
# 특히 이중 Legendary는 target 데이터 입니다. 모델이 학습하는 x에는 쓰지 않고, y에 사용한다

features = ['Total', 'HP', 'Attack', 'Defense','Sp. Atk', 'Sp. Def', 'Speed', 'Generation', 
            'name_count','long_name', 'Forme', 'Mega', 'Mewtwo','Deoxys', 'Kyurem', 'Latias', 'Latios',
            'Kyogre', 'Groudon', 'Hoopa','Poison', 'Ground', 'Flying', 'Normal', 'Water', 'Fire',
            'Electric','Rock', 'Dark', 'Fairy', 'Steel', 'Ghost', 'Psychic', 'Ice', 'Bug', 'Grass', 'Dragon', 'Fighting']
X = pokemon[features]
y = original_data[target]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=15)




# In[139]:


#이제 모델을 새롭게 사용해보겠습니다.
model = DecisionTreeClassifier(random_state=25)

model = DecisionTreeClassifier(random_state=25)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

result = confusion_matrix(y_test, y_pred)
print(f'TN: {result[0][0]} FR: {result[0][1]} FN: {result[1][0]} TP: {result[1][1]}')
print(f'정확도(TN + TP / Total) : {(result[0][0] + result[1][1])/ len(x_test) * 100}%')


# In[140]:


class_report = classification_report(y_test, y_pred)
print("\nClassification Report:")
print(class_report)


# In[ ]:





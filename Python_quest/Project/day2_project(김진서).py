import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

car_df = pd.read_csv('cars.csv')
brand_df = pd.read_csv('brand.csv')

car_df.head()
brand_df.head()

# car_df에서 브랜드 이름 추출 및 소문자로 변환
temp_df = car_df.copy()
temp_df['brand'] = temp_df['title'].str.split().str[0].str.lower()

# 브랜드 이름을 기준으로 국가 정보 매핑
brand_to_country = brand_df.set_index('title')['country'].to_dict()
temp_df['country'] = temp_df['brand'].map(brand_to_country)

# 'Engine' 컬럼의 'L' 문자 제거 및 숫자로 변환
temp_df['Engine'] = temp_df['Engine'].str.replace('L', '').astype(float)


#€

# 필요 없는 열 정리
total_df = temp_df.drop(columns=['brand'])

total_df = total_df.rename({'Engine' : 'Engine(L)'}, axis=1)


# 결측치가 한 개라도 있는 열 확인
columns_with_missing_values = total_df.columns[total_df.isna().any()].tolist()

# 결측치가 있는 열의 개수 계산
total_missing_columns_count = total_df.isna().any().sum()

# 결측치가 있는 열의 이름과 개수 출력
print("결측치가 한 개라도 있는 열:")
for column in columns_with_missing_values:
    missing_count = total_df[column].isna().sum()
    print(f"{column}: {missing_count}개의 결측치")

print("\n결측치가 있는 열의 개수:", total_missing_columns_count)


#이중에서 Previous Owner, Service history를 제외하고 없는건 모두 제거한다.

#결측치가 있는 걸 모두 제거함.
total_df = total_df.dropna(subset=['Engine(L)', 'Doors', 'Seats','Emission Class'])
total_df['Service history'] = total_df['Service history'].fillna('Unknown')


#Euro값을 int로 바꿉니다.
total_df['Emission Class'] = total_df['Emission Class'].str.replace('Euro', '').astype(int)
total_df['Doors'] = total_df['Doors'].astype(int)
total_df['Seats'] = total_df['Seats'].astype(int)

#문이 4개이하이되 0이아닌 데이터만 남깁니다.
total_df = total_df[(total_df['Doors'] != 0) & (total_df['Doors'] % 2 == 0) & (total_df['Doors'] <= 4)]

total_df['Mileage(miles)'].max() #208000
total_df['Mileage(miles)'].mean() #90453.34628975265

# MinMaxScaler를 사용하여 Mileage(miles) 열을 변환
minmax_scaler = MinMaxScaler()
total_df['Mileage_normalized'] = minmax_scaler.fit_transform(total_df[['Mileage(miles)']])

# StandardScaler를 사용하여 Mileage(miles) 열을 변환
standard_scaler = StandardScaler()
total_df['Mileage_standardized'] = standard_scaler.fit_transform(total_df[['Mileage(miles)']])


#PCA 사용해보기 scaler 사용
selected_columns = ['Price','Mileage(miles)'] #가격과, 거리간의 상관성을 알아봅니다.

for_pca_data = total_df[selected_columns]

scaler = StandardScaler()
scaled_data = scaler.fit_transform(for_pca_data)

# PCA 모델 생성
pca = PCA(n_components=0.7)  # 원본 데이터의 분산을 70% 이상 보존하는 주성분 추출
pca.fit(scaled_data)

# 주성분 변환
transformed_data = pca.transform(scaled_data)

print(scaled_data.shape)
print(transformed_data.shape)




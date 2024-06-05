import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 데이터 불러오기
df = pd.read_csv('data/trip.csv')

# 데이터 기본 정보 확인
print(df.info())
print(df.describe())
print(df.head())


# 결측치 유무와 비율 확인
missing_data = df.isnull().sum()
missing_percentage = (missing_data / len(df)) * 100
print(missing_percentage)

# 결측치 처리 (예: 결측치가 적은 경우 해당 행 제거)
df = df.dropna()


# 숫자형 변수 추출
numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns

# scatter plot 그리기
for column in numeric_columns:
    plt.figure(figsize=(10, 6))
    plt.scatter(df.index, df[column])
    plt.title(f'Scatter plot of {column}')
    plt.xlabel('Index')
    plt.ylabel(column)
    plt.show()

# 이상치 제거 (예: IQR 방법)
for column in numeric_columns:
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    df = df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]


# 시간 데이터 타입 변환
df['pickup_datetime'] = pd.to_datetime(df['pickup_datetime'])
df['dropoff_datetime'] = pd.to_datetime(df['dropoff_datetime'])

# 주행 시간 계산 (분 단위)
df['trip_duration'] = (df['dropoff_datetime'] - df['pickup_datetime']).dt.total_seconds() / 60

# 주행 시간, 주행 거리, 요금 간의 상관 관계 확인
correlation_matrix = df[['trip_duration', 'trip_distance', 'fare_amount']].corr()
sns.heatmap(correlation_matrix, annot=True)
plt.show()

# 결제 수단 통합
df['payment_type'] = df['payment_type'].replace({'Credit Card': 'Card', 'Debit Card': 'Card'})

# 최종 데이터 확인
print(df.info())
print(df.head())

# 정제된 데이터 저장
df.to_csv('trip_cleaned.csv', index=False)



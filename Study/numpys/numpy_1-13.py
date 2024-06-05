import pandas as pd
import os


csv_path = "data/covid19_italy_region.csv"
data = pd.read_csv(csv_path)
print(type(data))
#print(data)

print(data.head) #5개 출력
print(data.tail) #5개 출력

print(data.head(3)) #3개 출력
print(data.tail(3)) #3개 출력

print(f'{data.columns} 총 {len(data.columns)} 개')
print(data.info())

print(data.describe())
print(data.isnull().sum())
print(data['Country'].value_counts())
print(data['Country'].value_counts().sum())
print(data['RegionName'].value_counts().sum())

print("총 감염자", data['TotalPositiveCases'].sum())
print("전체 검사자 수", data['TestsPerformed'].sum())
print("사망자 수", data['Deaths'].sum())
print("회복자 수", data['Recovered'].sum())

print(data.sum())

print(data['TestsPerformed'].corr(data['TotalPositiveCases']))
print(data['TestsPerformed'].corr(data['Deaths']))
print(data['TotalPositiveCases'].corr(data['Deaths']))


'''
count(): NA를 제외한 수를 반환합니다.
describe(): 요약 통계를 계산합니다.
min(), max(): 최소, 최댓값을 계산합니다.
sum(): 합을 계산합니다.
mean(): 평균을 계산합니다.
median(): 중앙값을 계산합니다.
var(): 분산을 계산합니다.
std(): 표준편차를 계산합니다.
argmin(), argmax(): 최소, 최댓값을 가지고 있는 값을 반환합니다.
idxmin(), idxmax(): 최소, 최댓값을 가지고 있는 인덱스를 반환합니다.
cumsum(): 누적 합을 계산합니다.
pct_change(): 퍼센트 변화율을 계산합니다.

'''
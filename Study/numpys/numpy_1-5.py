import numpy as np

data1 = np.arange(12)#배열을 만듭니다. 단 안에있는 모든요소의 타입이 같아야합니다. list와는 다름!

data2 = np.array([1,2,3,4,5,6])#배열을 만듭니다. 단 안에있는 모든요소의 타입이 같아야합니다. list와는 다름! 

data3 = np.array([1,2,3,4,5,6,[7,8]], dtype=object) #내부의 원소의 타입은 object 타입으로 변함. (자바의 object와 비슷하다.) 명시해줘야 작동된다.

data4 = np.array([1,2,3,'4',5,6]) #내부의 원소의 타입은 모조리 str타입으로 변함

Array1 = data1.reshape(3, 4) #arange 12개의 원소로 되어있는 1차원 배열을만듭니다.  reshape(바꿀배열,(행,열)) 바꿀배열은 없어도 된다!
print(Array1.shape)
print(Array1.ndim)
print(Array1.size)

Array2 = np.reshape(data2,(3,2))
print(Array2.shape)
print(Array2.ndim)
print(Array2.size)


print(type(data1)) #해당 값 자체의 타입을 리턴 즉 리스트를 리턴함.
print(data1.dtype) #data1이 담고있는 데이터 타입을 반환.
print(data3.dtype)
print(data4.dtype)

#리스트의 값도 변환이 될까?
print(type(data3[0]))
print(type(data3[6]))

#앤왜 변환이 안될까?
print(type(data4[0]))
print(type(data4[3]))
'''
data3의 경우 dtype=object로 지정했기 때문에 각 요소가 개별 객체로 유지됩니다.
data4의 경우 하나의 요소가 문자열이기 때문에 Numpy는 자동으로 전체 배열의 타입을 str로 변환합니다.
'''

print(np.eye(3),'\n')

print(np.zeros([2,3]),'\n')

print(np.ones([3,3]),'\n')

matrix1 = np.arange(9).reshape(3,3)

print(matrix1,'\n')

print(matrix1 * 2,'\n')

print(matrix1 + 2,'\n')

print(matrix1 + 2,'\n')

matrix2 = np.arange(9).reshape(3,3)

print(matrix1 + matrix2,'\n')

matrix3 = np.arange(3)

print(matrix1 + matrix3,'\n') #[0,1,2]

print(np.array([1,2])+np.array([3,4]))
print(np.array([1,2])+3)

matrix4 = np.arange(9).reshape(3,3)
print(matrix4[0]) 
print(matrix4[:-1])


print(np.random.random())   # 0에서 1사이의 실수형 난수 하나를 생성합니다. 

print(np.random.randint(0,10))   # 0~9 사이 1개 정수형 난수 하나를 생성합니다. 

print(np.random.choice([0,1,2,3,4,5,6,7,8,9]))   # 리스트에 주어진 값 중 하나를 랜덤하게 골라줍니다.

print(np.random.permutation(10))   

print(np.random.permutation([0,1,2,3,4,5,6,7,8,9]))

# 이것은 정규분포를 따릅니다.
print(np.random.normal(loc=0, scale=1, size=5))    # 평균(loc), 표준편차(scale), 추출개수(size)를 조절해 보세요.

# 이것은 균등분포를 따릅니다. 
print(np.random.uniform(low=-1, high=1, size=5))  # 최소(low), 최대(high), 추출개수(size)를 조절해 보세요.

#A = np.arange(24).reshape(2,3,4)


import pandas as pd

# 브랜드와 국가 정보를 포함하는 데이터 프레임
brand_data = {
    'title': ['skoda', 'vauxhall', 'hyundai', 'mini', 'ford', 'volvo', 'peugeot', 'bmw', 'citroen', 'mercedes-benz',
              'mazda', 'saab', 'volkswagen', 'honda', 'mg', 'toyota', 'seat', 'nissan', 'alfa', 'renault',
              'kia', 'proton', 'fiat', 'audi', 'mitsubishi', 'lexus', 'land', 'chevrolet', 'suzuki', 'dacia',
              'daihatsu', 'jeep', 'jaguar', 'chrysler', 'rover', 'ds', 'daewoo', 'dodge', 'porsche', 'subaru',
              'infiniti', 'abarth', 'smart', 'marcos', 'maserati', 'ssangyong', 'lagonda', 'isuzu'],
    'country': ['Czech Republic', 'United Kingdom', 'South Korea', 'United Kingdom', 'United States', 'Sweden',
                'France', 'Germany', 'France', 'Germany', 'Japan', 'Sweden', 'Germany', 'Japan', 'United Kingdom',
                'Japan', 'Spain', 'Japan', 'Italy', 'France', 'South Korea', 'Malaysia', 'Italy', 'Germany', 'Japan',
                'Japan', 'United Kingdom', 'United States', 'Japan', 'Romania', 'Japan', 'United States', 'United Kingdom',
                'United States', 'United Kingdom', 'France', 'South Korea', 'United States', 'Germany', 'Japan', 'Japan',
                'Italy', 'Germany', 'United Kingdom', 'Italy', 'South Korea', 'United Kingdom', 'Japan']
}

brand_df = pd.DataFrame(brand_data)

# 자동차 모델과 엔진 정보를 포함하는 데이터 프레임
car_data = {
    'title': ['SKODA FABIA', 'BMW X5', 'TOYOTA COROLLA', 'HONDA CIVIC', 'AUDI A4'],
    'Engine': ['1.4L', '2.0L', '1.8L', '1.6L', '2.0L']
}

car_df = pd.DataFrame(car_data)

# car_df에서 브랜드 이름 추출 및 소문자로 변환
car_df['brand'] = car_df['title'].str.split().str[0].str.lower()

# 브랜드 이름을 기준으로 국가 정보 매핑
brand_to_country = brand_df.set_index('title')['country'].to_dict()
car_df['country'] = car_df['brand'].map(brand_to_country)

# 'Engine' 컬럼의 'L' 문자 제거 및 숫자로 변환
car_df['Engine'] = car_df['Engine'].str.replace('L', '').astype(float)

# 필요 없는 열 정리
car_df.drop(columns=['brand'], inplace=True)

# 최종 결과 확인
print(car_df)

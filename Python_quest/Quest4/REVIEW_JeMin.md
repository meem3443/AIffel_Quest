# AIFFEL Campus Code Peer Review Templete
- 코더 : 김진서
- 리뷰어 : 유제민

# PRT(Peer Review Template)
[ ]  **1. 주어진 문제를 해결하는 완성된 코드가 제출되었나요?**
- 문제에서 요구하는 기능이 정상적으로 작동하는지?
    - 해당 조건을 만족하는 부분의 코드 및 결과물을 근거로 첨부
- def numberInput():
  while True:
    try:
      number1 = int(input("숫자 첫번째를 입력해주세요"))
      number2 = int(input("숫자 두번째를 입력해주세요"))
      return [number1, number2]

    except ValueError:
      print("잘못된 숫자 입력입니다. 정수를 입력해주세요")

- def operatorInput():

  while True:
    try:

      operator = input("연산자를 입력해주세요 [+,-,*,-,**]")

      if operator == '+':
        return '+'

      if operator == '-':
        return '-'

      if operator == '*':
        return '*'

      if operator == '/':
        return '/'

      if operator == '**':
        return '**'

      else:
        raise Exception

    except Exception:
      print("잘못된 연산자 입력입니다.")

- def operationDo(listInputed,operatorInputed):
  number1 = listInputed[0]
  number2 = listInputed[1]
  operator = operatorInputed

  try:
    if operator == '+':
        return number1 + number2

    if operator == '-':
        return number1 - number2

    if operator == '*':
        return number1 * number2

    if operator == '/':
        return number1 / number2

    if operator == '**':
        return m.pow(number1,number2)
  except ZeroDivisionError:
    print("0으로 나누기 에러가 발생했습니다.")
    return False

- 숫자 입력, 연산자 입력, 숫자 계산을 각각 함수로 만들어서 진행
    
[ ]  **2. 핵심적이거나 복잡하고 이해하기 어려운 부분에 작성된 설명을 보고 해당 코드가 잘 이해되었나요?**
- 해당 코드 블럭에 doc string/annotation/markdown이 달려 있는지 확인
- 해당 코드가 무슨 기능을 하는지, 왜 그렇게 짜여진건지, 작동 메커니즘이 뭔지 기술.
- 주석을 보고 코드 이해가 잘 되었는지 확인
    - 잘 작성되었다고 생각되는 부분을 근거로 첨부합니다.
- def operationDo(listInputed,operatorInputed):

  #번외 : 연산을 처리할떄는 아래와 같은 예외가 존재합니다.
  '''
  1. 전자의 숫자가 '0'일때
    1. *,/는 무조건 결과값이 0이 됩니다.
    2. +라면 후자의 숫자가 결과값입니다.
    3. -라면 후자의 숫자의 -1을 곱한 것이 결과값입니다.

  2. 후자의 숫자가 '0'일때
    1. /는 에러를 발생시킵니다.
    2. *라면 무조건 결과값이 0이됩니다.
    3. +,-라면 전자의 숫자가 결과값입니다.

  3. 둘다 0일때
    1. /는 에러를 발생시킵니다.
  '''
  number1 = listInputed[0]
  number2 = listInputed[1]
  operator = operatorInputed

  try:
    if operator == '+':
        return number1 + number2

    if operator == '-':
        return number1 - number2

    if operator == '*':
        return number1 * number2

    if operator == '/':
        return number1 / number2

    if operator == '**':
        return m.pow(number1,number2)
  except ZeroDivisionError:
    print("0으로 나누기 에러가 발생했습니다.")
    return False

 - 연산하는 내용에 대해 설명이 자세히 나와있습니다.
  
[ ]  **3. 에러가 난 부분을 디버깅하여 “문제를 해결한 기록”을 남겼나요? 또는 “새로운 시도 및 추가 실험”을 해봤나요?**
- 문제 원인 및 해결 과정을 잘 기록하였는지 확인
- 문제에서 요구하는 조건에 더해 추가적으로 수행한 나만의 시도, 실험이 기록되어 있는지 확인
    - 잘 작성되었다고 생각되는 부분을 캡쳐해 근거로 첨부합니다.
- 문제를 해결한 기록 또는 새로운 시도 및 추가 실험 은 없었습니다.
        
[ ]  **4. 회고를 잘 작성했나요?**
- 프로젝트 결과물에 대해 배운점과 아쉬운점, 느낀점 등이 상세히 기록 되어 있나요?
- 딥러닝 모델의 경우, 인풋이 들어가 최종적으로 아웃풋이 나오기까지의 전체 흐름을 도식화하여 모델 아키텍쳐에 대한 이해를 돕고 있는지 확인
- 진서님이 함수로 작성한 것과 동규님이 작성한 코드를 비교하면서 사람마다 코드를 짜는것이 다를 수 있다는걸 회고함
        
[ ]  **5. 코드가 간결하고 효율적인가요?**
- 파이썬 스타일 가이드 (PEP8)를 준수하였는지 확인
- 코드 중복을 최소화하고 범용적으로 사용할 수 있도록 모듈화(함수화) 했는지
    - 잘 작성되었다고 생각되는 부분을 근거로 첨부합니다.
- 모든 동작을 함수화 해서 상당히 간결했다 생각합니다.

# 참고 링크 및 코드 개선


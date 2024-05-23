# AIFFEL Campus Code Peer Review Templete

-   코더 : 김진서, 유제민
-   리뷰어 : 소다흰

# PRT(Peer Review Template)

\[ \] **1\. 주어진 문제를 해결하는 완성된 코드가 제출되었나요?**

-   문제에서 요구하는 기능이 정상적으로 작동하는지?
    -   해당 조건을 만족하는 부분의 코드 및 결과물을 근거로 첨부
    -   \-> 1번 과제

```
def find_min_max(numbers):
    min_value = float('inf')
    max_value = float('-inf')

    def update_min_max(num):
        nonlocal max_value, min_value
        if num > max_value:
            max_value = num
        if num < min_value:
            min_value = num

    for num in numbers:
        update_min_max(num)

    def get_min():
        return min_value

    def get_max():
        return max_value

    return get_min, get_max
```

      -> 2번 과제

```
def counter(fn):
    tryCount = 0
    def deco():
        nonlocal tryCount
        tryCount = tryCount + 1
        fn()
        print('{0} 실행횟수:{1} '.format(fn.__name__,tryCount))
    return deco

@counter
def say_hello():
    print("Hello Aiffel!")

for i in range(5):
    say_hello()
```

\[ \] **2\. 핵심적이거나 복잡하고 이해하기 어려운 부분에 작성된 설명을 보고 해당 코드가 잘 이해되었나요?**

-   해당 코드 블럭에 doc string/annotation/markdown이 달려 있는지 확인
-   해당 코드가 무슨 기능을 하는지, 왜 그렇게 짜여진건지, 작동 메커니즘이 뭔지 기술.
-   주석을 보고 코드 이해가 잘 되었는지 확인
    -   잘 작성되었다고 생각되는 부분을 근거로 첨부합니다. -> 3과 답변이 동일합니다.

\[ \] **3\. 에러가 난 부분을 디버깅하여 “문제를 해결한 기록”을 남겼나요? 또는 “새로운 시도 및 추가 실험”을 해봤나요?**

-   문제 원인 및 해결 과정을 잘 기록하였는지 확인
-   문제에서 요구하는 조건에 더해 추가적으로 수행한 나만의 시도, 실험이 기록되어 있는지 확인
    -   잘 작성되었다고 생각되는 부분을 캡쳐해 근거로 첨부합니다. -> 1번 과제 시, 아래와 같이 문제 해결 과정을 남겼습니다.  
          
        

```
    def update_min_max(num):
        # 외부함수의 변수인 min_value, max_value 참조
        # 처음 코드를 작성할 때 nonlocal 에 대한 개념이 확실하게 잡히지 않아서 없어도 상위 변수 값을 가져올 수 있다고 생각했음
        # nonlocal 없이 실행 했을 때 UnboundLocalError: cannot access local variable 'max_value' where it is not associated with a value 에 대한 오류가 나왔고
        # 외부함수의 변수를 호출하지 못 하는 것을 알게 되어 nonlocal을 추가
        nonlocal max_value
        nonlocal min_value

        # 만약 num 값이 min_value보다 작다면 min_value를 num 값으로 변경
        if num > max_value:
          max_value = num

        # 만약 num 값이 max_value보다 크다면 max_value를 num 값으로 변경
        if num < min_value:
          min_value = num
```

\[ \] **4\. 회고를 잘 작성했나요?**

-   프로젝트 결과물에 대해 배운점과 아쉬운점, 느낀점 등이 상세히 기록 되어 있나요?
    -   딥러닝 모델의 경우, 인풋이 들어가 최종적으로 아웃풋이 나오기까지의 전체 흐름을 도식화하여 모델 아키텍쳐에 대한 이해를 돕고 있는지 확인 -> 네, 두분 다 상세히 작성해주셨습니다.

\[ \] **5\. 코드가 간결하고 효율적인가요?**

-   파이썬 스타일 가이드 (PEP8)를 준수하였는지 확인
-   코드 중복을 최소화하고 범용적으로 사용할 수 있도록 모듈화(함수화) 했는지
    -   잘 작성되었다고 생각되는 부분을 근거로 첨부합니다. -> 중간의 문제 해결과정을 거쳐서 올바른 결과값을 내는 코드를 완성하셨습니다.

# 참고 링크 및 코드 개선

```
# 코드 리뷰 시 참고한 링크가 있다면 링크와 간략한 설명을 첨부합니다.
# 코드 리뷰를 통해 개선한 코드가 있다면 코드와 간략한 설명을 첨부합니다.
```

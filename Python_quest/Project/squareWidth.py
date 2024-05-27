# 사각형 넓이를 구하는 클래스 완성!
class Square:
    def __init__(self):
        self.square = int(input('넓이를 구하고 싶은 사각형의 숫자를 써주세요.\n 1.직사각형 2.평행사변형 3.사다리꼴 \n >>>'))

        if self.square == 1:
            print('직사각형 함수는 rect()입니다.')
            self.rect()

        elif self.square == 2:
            print('평행사변형 함수는 par()입니다.')
            self.par()
        elif self.square == 3:
            print('사다리꼴 함수는 trape()입니다.')
            self.trape()
        
        else:
            print('1, 2, 3 중에서 다시 입력해주세요')

    def rect(self):
        width, vertical = map(int, input('가로, 세로를 입력하세요. 예시 : 가로,세로\n >>>').split(','))
        area = width * vertical
        result = '직사각형의 넓이는 : ' + str(area)
        print(result)
        return result

    def par(self):
        width,height = map(int, input("밑변,높이를 각각 입력하시오").split(","))
        result = width * height
        print(result)
        return result
    def trape(self):
        width,upper,height = map(int, input("밑변,윗변,높이를 각각 입력하시오").split(","))
        result = (width + upper) * height/2
        print(result)
        return result
        

a = Square()  

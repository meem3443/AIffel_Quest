import random as r


class Aiffel:

    membershipCount = "00"

    coreDict = []

    def __init__(self, name, YY, NN, C):
        try:
            # 모두 숫자로 변환하여 저장
            self.name = name
            self.YY = int(YY)
            self.NN = int(NN)
            self.C = int(C)
            self.code = ""

            self.score = 0
            self.penalty = 0
            self.total = 0

            Aiffel.coreDict.append(self)
        except ValueError:
            # 숫자로 변환할 수 없는 경우 예외 처리
            print("YY, NN, C 는 반드시 숫자여야합니다.")

        else:
            # 클래스 변수 membershipCount를 사용하여 코드 생성
            formatted_membershipCount = str(Aiffel.membershipCount).zfill(2)
            self.code = f"{self.YY}{self.NN}{self.C}{formatted_membershipCount}"
            Aiffel.membershipCount = str(int(Aiffel.membershipCount) + 1).zfill(2)

    def getId(self):
        return self.code

    def getName(self):
        return self.name

    def scoreAdd(self, target, num):  # Q2 점수관리 메서드. 점수부여
        for i in Aiffel.coreDict:
            if i.getId() == target:
                i.score = i.score + num
                i.total = i.score - i.penalty

    def penaltyAdd(self, target, num):  # Q2 점수관리 메서드. 페널티 부여
        for i in Aiffel.coreDict:
            if i.getId() == target:
                i.penalty = i.penalty + num
                i.total = i.score - i.penalty

    def show(self):  # Q2 현재 총점및 정보 모두 개인 출력
        print(
            f"이름 : {self.name} 학번 : {self.code} 점수 : {self.score} 페널티 : {self.penalty} 총점 : {self.total}"
        )

    def showAll(self, type):  # Q3 현재 총점 전체출력, type값에 따라 정렬후 출력
        if type == "total":  # 총점 기준 정렬
            print("\n________________________________\n")
            print("총점 내림차순 정렬")
            print("________________________________\n")
            for grew in self.sort_by_total():
                grew.show()
            print("\n________________________________\n")
        elif type == "score":  # 얻은 점수 기준 정렬
            print("\n ________________________________\n")
            print("점수 내림차순 정렬")
            print("________________________________\n")
            for grew in self.sort_by_score():
                grew.show()
            print("\n________________________________\n")

        elif type == "penalty":  # 얻은 페널티 기준 정렬
            print("\n________________________________\n")
            print("페널티 내림차순 정렬")
            print("________________________________\n")
            for grew in self.sort_by_penalty():
                grew.show()
            print("\n________________________________\n")

        else:
            print("\n________________________________\n")
            print("입력순서대로 출력")
            print("________________________________\n")
            for grew in Aiffel.coreDict:
                grew.show()
            print("\n________________________________\n")

    # score 기준으로 정렬
    def sort_by_score(self):  # 정렬된 리스트 변환
        sorted_list = sorted(Aiffel.coreDict, key=lambda x: x.score, reverse=True)
        return sorted_list

    # penalty를 기준으로 정렬
    def sort_by_penalty(self):  # 정렬된 리스트 변환
        sorted_list = sorted(Aiffel.coreDict, key=lambda x: x.penalty, reverse=True)
        return sorted_list

    # total을 기준으로 정렬
    def sort_by_total(self):
        sorted_list = sorted(Aiffel.coreDict, key=lambda x: x.total, reverse=True)
        return sorted_list

    def deleteMan(self, target):  # Q3 특정인 제거
        for i in Aiffel.coreDict:
            if i.getId() == target:
                print(f"[{target}이 성공적으로 제거되었습니다.]\n")
                Aiffel.coreDict.remove(i)

    def grouping(
        self, groupSize
    ):  # Q4 그루핑 기능 큐를 사용한다. 일단 섞어서 큐에 넣고 pop통해서 값을 가져온다. 이후 남은인원이 그룹사이즈보다 작으면 전부 거기다가 추가한다.
        if groupSize > 1 and groupSize < 5:
            que = Aiffel.coreDict
            r.shuffle(que)
            result = []
            while len(que) != 0:
                temp = []
                for i in range(groupSize):
                    if len(que) != 0:
                        temp.append(que.pop())
                    else:
                        break
                result.append(temp)

            print("________________________________\n")
            for i in range(len(result)):
                print(f"{i+1}팀: ", end="")
                for j in result[i]:
                    print(f"{j.getName()} ", end="")
                print()
            print("________________________________\n")
            return result
        else:
            print("2~4의 입력이 필요합니다.")


def main():
    a = Aiffel("김진서", 24, 31, 1)
    b = Aiffel("이승준", 24, 31, 1)
    c = Aiffel("남유빈", 24, 31, 1)
    d = Aiffel("홍길동", 24, 31, 1)
    e = Aiffel("홍길자", 24, 31, 1)
    f = Aiffel("이시완", 24, 31, 1)
    g = Aiffel("차은우", 24, 31, 1)

    a.scoreAdd("2431100", 100)
    b.scoreAdd("2431101", 300)
    c.penaltyAdd("2431102", 1000)
    d.scoreAdd("2431103", 10)
    e.scoreAdd("2431104", 100)
    f.scoreAdd("2431105", 1000)
    g.scoreAdd("2431106", 10000)

    a.showAll("total")  # 총점을 기준으로 정렬합니다.

    a.showAll("penalty")  # 쌓인 패널티를 기반으로 정렬합니다.

    a.showAll("score")  # 얻은 점수를 기반으로 정렬합니다.

    a.deleteMan(
        "2431100"
    )  # 특정 학번을 지웁니다. 이름은 겹칠 수 있기에 학번으로 지정합니다.

    a.showAll(
        "default"
    )  # total, penalty, score가 아니라면 무조건 넣은순서대로 출력합니다.

    a.grouping(4)  # 두명씩 묶습니다.


main()

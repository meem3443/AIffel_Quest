import random as r
import math as m
import time as t
import os

# os.system('cls') # window
# os.system('clear') # linux, mac


class Character:

    def __init__(self, name, level, health, attack, defense, speed):

        self.name = name
        self.speed = speed
        self.level = level
        self.health = health
        self.attack = attack
        self.defense = defense

    def __str__(self):

        return f"이름: {self.name}, 레벨: {self.level}, 체력: {self.health}, 공격력: {self.attack}, 방어력: {self.defense}"

    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False

    def take_damage(self, damage):
        self.damage = damage
        if self.is_alive():
            if (self.damage - self.defense) > 0:
                self.health -= self.damage - self.defense
            else:
                self.damage = 0

    def attack_target(self, target):
        self.attack_real = r.randint(self.attack // 2, self.attack)
        target.take_damage(self.attack_real)
        return self.attack_real


"""
super().__init__(name, level=1, health=100, attack=25, defense=5)
        self.experience = 0
"""


class Player(Character):

    def __init__(self, name):

        self.name = name
        self.experience = 0

        super().__init__(name, level=1, health=100, attack=25, defense=5, speed=3)

    def gain_experience(self, exp):
        self.experience += exp
        if self.experience >= 50:
            n = self.experience // 50
            for i in range(n):
                self.level_up()
                self.experience -= 50

    def level_up(self):
        self.level += 1
        self.attack += 10
        self.defense += 5
        self.speed += 2
        print("레벨업!")


class Monster(Character):
    def __init__(self, name, level, speed):
        """
        health = math.floor(100 * (level * 0.25))
        attack = math.floor(5 * (level * 0.25))
        defense = math.floor(2 * (level * 0.25))
        super().__init__(name, level, health, attack, defense)
        """

        self.name = name
        self.level = level
        self.health = m.floor(1 * (self.level * 1.25))
        self.attack = m.floor(5 * (self.level * 1.25))
        self.defense = m.floor(2 * (self.level * 1.25))
        self.speed = m.floor(speed * (self.level * 1.25))

        super().__init__(name, level, self.health, self.attack, self.defense, speed)


"""
def __init__(self, name, level):
        health = 100 * (level * 0.25)
        attack = 5 * (level * 0.25)
        defense = 5  # 방어력은 임의로 설정
        super().__init__(name, level, health, attack, defense)

"""


def monster_gen(monster_info, count):
    monster_names = list(monster_info.keys())
    for i in range(count):
        # 랜덤으로 몬스터 이름 선택
        monster_name = r.choice(monster_names)
        # 선택된 몬스터의 최대 레벨
        max_level = monster_info[monster_name]
        yield Monster(monster_name + str(i), r.randint(1, max_level), r.randint(1, 10))



def battle(Player, dungeon):
    while True:
        try:
            Monster = next(dungeon)
            while Monster.is_alive() and Player.is_alive():
                t.sleep(5)
                player_attack_damage_total = Player.attack_target(Monster)
                print(
                    f"{Player.name}가 {Monster.name}를 공격하여. {player_attack_damage_total}만큼의 데미지를 입혔습니다.\n"
                )
                print(Player.__str__())

                t.sleep(5)
                print(
                    f"{Monster.name}가 {Player.name}를 공격하여. {Monster.attack_target(Player)}만큼의 데미지를 입혔습니다.\n"
                )

                if not Monster.is_alive():
                    Monster.health = 0

                print(Monster.__str__())

                if Player.is_alive():
                    print(
                        f"플레이어가 살아남아 {int(player_attack_damage_total * 0.1)}만큼의 경험치를 얻었습니다."
                    )
                    Player.gain_experience(int(player_attack_damage_total * 0.1))

                elif not Player.is_alive():
                    print("플레이어가 사망했습니다.")
                    return

                if Monster.is_alive():
                    continue
                elif not Monster.is_alive():
                    print("적 처치!")
                    Monster = next(dungeon)

        except StopIteration:  # 플레이어가 모두 잡아버렸다
            print("전원처치")
            return
def attack_first(Player, Monster):

    while True :

        player_speed = Player.speed + r.randint(1,12)
        monster_speed = Monster.spped + r.randint(1,12)

        if player_speed > monster_speed:
            return Player,Monster
        
        elif player_speed < monster_speed:
            return Monster,Player
        
        else:
            continue




def main():
    monster_info = {
    '고블린': 3,
    '오크': 5,
    '드래곤': 10,
    # 원하는 다른 몬스터를 추가할 수 있습니다.
}

    # 제너레이터 생성
    gen = monster_gen(monster_info, 3)  # 몬스터 생성기. 여러개 만들면됨. 이게곧 챕터.

    # 제너레이터에서 몬스터 객체 출력
    # print(next(gen))  # 출력: 몬스터 객체 (예: 이름: 고블린, 레벨: 3, 체력: 75.0, 공격력: 3.75, 방어력: 5)
    # print(next(gen))  # 출력: 몬스터 객체 (예: 이름: 고블린, 레벨: 1, 체력: 25.0, 공격력: 1.25, 방어력: 5)
    # print(next(gen))  # 출력: 몬스터 객체 (예: 이름: 고블린, 레벨: 4, 체력: 100.0, 공격력: 5.0, 방어력: 5)

    player = Player(input("플레이어 이름을 입력하세요"))

    battle(player, gen)


main()

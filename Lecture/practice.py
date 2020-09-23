class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed

class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage
        
    def attack(self, location):
        print("현재 {0} 유닛이 {1} 방향으로 공격하고 있습니다. [공격력 : {2}]".format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1}의 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 체력은 {1}입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 : {2}]".format(self.name, location, self.speed))

class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
        
    def fly(self, name, location):
        print("{0} 유닛이 {1} 방향으로 날아가고 있습니다. [속도 : {2}]".format(name, location, self.flying_speed))

class FlyableAttackUnit(Flyable, AttackUnit):
    def __init__(self, name, hp, damage, speed, flying_speed):
        AttackUnit.__init__(self, name, hp, damage, speed)
        Flyable.__init__(self, flying_speed)
    
    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        #Unit.__init__(self, name, hp, 0) # 건물에 speed가 없으므로 0으로 처리
        super().__init__(name, hp, 0)
        self.location = location
        print("{0}이 생성되었습니다. 체력 : {1}, 위치 : {2}".format(name, hp, location))


supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")

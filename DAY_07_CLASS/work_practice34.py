# 클래스 사용하기

# 클래스 만들기 --------------------------------------------------------------------------
class Person:
    # 속성 사용
    def __init__(self):
        self.hello = '안녕하세요'
    def greeting(self):
        print(self.hello)

# 인스턴스 = 클래스()
james = Person()

# 메서드 호출
james.greeting()


# 인스턴스 만들 때 값 받기 -------------------------------------------------------------------
class Person2:
    def __init__(self, name, age, address):
        self.hello = 'Hello'
        self.name = name
        self.age = age
        self.address = address

    def greeting(self):
        print('{0} 저는 {1}입니다.' .format(self.hello, self.name))

maria = Person2('마리아', 20, '서울시')
maria.greeting()

print(f'이름 : {maria.name}\n나이: {maria.age}\n주소: {maria.address}')

# 비공개 속성 사용 -----------------------------------------------------------------------------
class Person3:
    def __init__(self, name, age, address, wallet):
        self.hello = 'Hello'
        self.name = name
        self.age = age
        self.address = address
        self.__wallet = wallet

    def pay(self, amount):
        self.__wallet -= amount
        print('이제 {0}원' .format(self.__wallet))

maria = Person3('마리아', 20, '서울시', 10000)
maria.pay(3000)

# 연습문제 -----------------------------------------------------------------
class Knight:
    def __init__(self, health, mana, armor):
        self.health = health
        self.mana = mana
        self.armor = armor

    def slash(self):
        print('Cut')

x = Knight(542.4, 210.3, 38)
print(x.health, x.mana, x.armor)
x.slash()

# 심사문제 ------------------------------------------------------------------

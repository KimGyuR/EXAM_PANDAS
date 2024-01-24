# 클래스 속성 사용
class Person:
    bag = []

    def put_bag(self, stuff):
        self.bag.append(stuff)

james = Person()
james.put_bag('book')

maria = Person()
maria.put_bag('key')

print(james.bag, maria.bag)

# 인스턴스 속성 사용
class Person2:
    def __init__(self):
        self.bag = []

    def put_bag(self, stuff):
        self.bag.append(stuff)

james = Person2()
james.put_bag('book')

maria = Person2()
maria.put_bag('key')

print(james.bag, maria.bag)

# 정적 메서드 사용
class Calc:
    @staticmethod
    def add(a, b):
        print(a+b)

    @staticmethod
    def multi(a, b):
        print(a * b)

Calc.add(10,20)
Calc.multi(10,20)

# 클래스 메서드 사용
class Person3:
    count = 0

    def __init__(self):
        Person3.count += 1

    @classmethod
    def print_count(cls):
        print('{0}명 생성되었습니다.'.format(cls.count))

james=Person3()
maria=Person3()

Person3.print_count()

# 연습문제
class Date:
    @staticmethod
    def is_date_valid(date_string):
        year, month, day = map(int, date_string('-'))
        return month <= 12 and day <= 31

if Date.is_date_valid('2000-10-31'):
    print('올바른 날짜 형식입니다.')
else:
    print('잘못된 날짜 형식입니다.')


# 심사문제
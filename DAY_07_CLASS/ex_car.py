# -------------------------------------------------------
# 자동차 클래스
# 클래스 이름 : Car
# 클래스속성 : (바퀴, 색상, 차번호, 차종류(인스턴스 속성)), 제조사(클래스 속성)
# 클래스기능 : 주행한다, 정지한다. 후진하다
# -------------------------------------------------------
class Car:
    # 클래스 정의
    maker='현대'

    # 생성자 메서드 => 객체 즉, 인스턴스 생성 메서드
    def __init__(self, wheel, color, number, kind):
        # 힙 영역에 저장
        self.wheel = wheel
        self.color = color
        self.number = number
        self.kind = kind

    # 객체 즉, 카 인스턴스 메서드
    def driving(self, where):
        print(f'{where}에 {self.number} 차가 주행하고 있다.')
    def stop(self, place):
        print(f'{self.number} 차가 {place}에 정지하고 있다.')
    def back(self):
        print(f'{self.number} 차가 후진한다')

# -----------------------------------------------------------
# 자동차 인스턴스 생성
# -----------------------------------------------------------
myCar=Car(19,'red', '1111', '새단')
secondCar = Car(20, 'hotpink', '7777', 'SUV')

# 자율주행자동차 클래스 생성 : 상속적용하기
# AutoCar에 Car를 상속함 => Car의 클래스 기능 사용 가능
class AutoCar(Car):

    def __init__(self, wheel, color, number, kind, auto):
        super().__init__(wheel, color, number, kind)
        self.auto=auto

# 자율비행자동차 클래스 생성 : 상속적용하기
# FlyAutoCar에 AutoCar(Car를 상속받은 상태)를 상속함 => Car와 AutoCar 두 가지 클래스를 기능 사용 가능
class FlyAutoCar(AutoCar):

    def __init__(self, wheel, color, number, kind, auto, fly):
        super().__init__(wheel, color, number, kind, auto)
        self.fly=fly


AC = AutoCar(25,'blue', '1234', '새단','On')
FAC = FlyAutoCar(30,'sky_blue', '2330', '디젤','Off', 'Flying')

# 상속받은 Car에 있는 메서드 사용
AC.back()
FAC.driving('Daegu')

print(AC.wheel, AC.color, AC.number, AC.kind, AC.auto)
print(FAC.wheel, FAC.color, FAC.number, FAC.kind, FAC.auto, FAC.fly)
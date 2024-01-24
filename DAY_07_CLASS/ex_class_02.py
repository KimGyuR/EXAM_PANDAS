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



# ----------------------------------------------------------------------
# 사랑 클래스
# 클래스 이름 : Love
# 클래스속성 : kind(종류)
# 클래스기능 : 새우까주기, 깻잎떼주기, 금융치료하기, 데려다주기, 데이트하기, 같이아프기
#            대신죽어주기, 희생하기
# -----------------------------------------------------------------------
class Love:

    # 생성자 메서드 => 객체 즉, 인스턴스 생성 메서드
    def __init__(self, kind):
        self.kind = kind

    # 객체 즉, 사랑 인스턴스 메서드
    def shrip(self):
        pass
    def leaf(self):
        pass
    def moneyheal(self):
        pass
    def goback(self):
        pass
    def bgdate(self):
        pass
    def hurt(self):
        pass
    def insteadD(self):
        pass
    def sacri(self):
        pass

# ----------------------------------------------------------------------
# 계산기 클래스
# 클래스 이름 : calC
# 클래스속성 : 브랜드, 종류, 색깔, 크기, 가격
# 클래스기능 : 덧셈, 뺄셈, 곱셈, 나눗셈
# - 데이터 => 속성 또는 기능에서 매개변수
# -----------------------------------------------------------------------
class calC:
    # 클래스 변수
    maker = 'casio'
    __size=(7,15)        # 비공개 속성 __ 속성명 : 클래스 밖에서 속성 읽거나/쓰기 불가

    # 객체 즉 인스턴스 생성 메서드
    def __init__(self, kind, color, price, info):
        self.kind = kind
        self.color = color
        self.price = price
        self.__info = info      # 인스턴스 생성 시 계산기에 각인되는 정보
        self.data=0

    # 비공개 인스턴스 속성 읽기/쓰기(getter/setter) 메서드
    def getInfo(self):
        return self.__info

    def setInfo(self, info):
        self.__info=info

    # 비공개 인스턴스 속성 읽기/쓰기(getter/setter) 메서드
    # => 속성 읽기/쓰기 방식으로 동작하도록 설정
    @property
    def info(self): return self.__info

    @info.setter
    def info(self, info):
        self.__info=info

    # 덧셈 기능
    def plus(self, nums):
        self.data += nums

    def minus(self, nums):
        self.data -= nums

    def multi(self, nums):
        self.data *= nums

    def div(self, nums):
        if not nums: return '0으로 나눌 수 없습니다.'
        self.data = self.data/nums

    def result(self):
        return self.data

# ----------------------------------------------------------------------
# claC 클래스로 인스턴스 생성 => 힙에 생성: 인스턴스변수 + 클래스 변수
#                                     인스턴스 메서드 사용 가능
# ----------------------------------------------------------------------
c1=calC('engineering', 'black',10000, '홍길동계산기')

# 인스턴스 속성 읽기 => 공개 속성만 읽기 가능
print(c1.data, c1.color, c1.kind)

# 인스턴스 속성 변경 => 공개 속성만 읽기 가능
c1.color = '빨간색'

# 인스턴스 비공개 속성 읽기 ==> 전용에 매서드 getter/setter 통해서 읽기/쓰기
print(c1.getInfo(), c1.info)

# 인스턴스 비공개 속성 변경 ==> 전용에 매서드 getter/setter 통해서 읽기/쓰기
c1.setInfo("내꺼")
c1.info="내꺼임~~~"

print(c1.getInfo(), c1.info)

# ----------------------------------------------------------------------
# claC 클래스로 계산기 정보 확인 => 클래스 변수만 확인 가능
#                              인스턴스 변수나 메서드 사용 불가능!!
#                              self 값이 없음!
# ----------------------------------------------------------------------
print(calC.maker)

# 인스턴스 메서드에 접근 불가!!
#print(calC.plus(10,2))
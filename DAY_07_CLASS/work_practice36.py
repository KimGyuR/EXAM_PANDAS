# 사람 클래스로 학생 클래스 만들기
class Person:
    def greeting(self):
        print('Hello')

class Student(Person):
    def study(self):
        print('study')

james = Student()
james.greeting()
james.study()

# 메서드 오버라이딩
class Person2:
    def greeting(self):
        print('Hello')

class Student2(Person2):
    def greeting(self):
        print("Hello, I'm a student")

james = Student2()
james.greeting()
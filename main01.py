# 클래스 정의(선언) : 붕어빵 틀 
class User: 
    def __init__ (self, name):     # 생성자 : 클래스가 처음 생성될 때 자동으로 호출
        self.name = name           # 변수를 초기화 

    def show(self):                # 메서드(Method)
        return f"회원 이름: {self.name}"


# 인스턴트 생성 : 붕어빵 만들기 
user_a = User("손흥민")
user_b = User("이강민")

# User 클래스로 생성한 인스턴스 (메모리에 생성)


# 클래스의 인스턴스 변수
print(user_a.name)
print(user_b.name)


# 클래스의 메서드 접근
print(user_a.show())
print(user_b.show())




print(type(user_a))
print(user_a is user_b)
print(id(user_a))
print(id(user_b))

# ========================================================

class Monitor:
    def display_info(self): 
        #인스턴트 변수
        self.resolution = "1920X1080"
        self.size = "27d인치"
        print(f"모니터 정보\n해상도: {self.resolution}\n크기: {self.size}\n객체 ID: {id(self)}")         # \n = 엔터키 역할


monitor = Monitor()     # 객체(인스턴스) 생성 (모니터 객체 생성)
print(id(monitor))      # 모니터 인스턴스의 id 출력 

monitor.display_info()


# =========================================================

class SmartPhone:
    def __init__(self, model): 
        self.model = model          # 속성(Attribute)
        self.battery = 50          # 속성(Attribute)


    def charge(self, amount): 
        self.battery += amount
        if self.battery > 100:
            self.battery = 100 
            print(f"배터리 충전 완료 : {self.battery}%")
        else:
            print(f"배터리 충전 중 ... : {self.battery}%")
            

phone_a = SmartPhone("아이폰")
print(phone_a.model)
phone_a.charge(30)
phone_a.charge(30)

phone_b = SmartPhone("갤럭시")



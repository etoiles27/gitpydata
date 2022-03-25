class Car:
    speed = 0
    color = 'white'
    tire = 4
    def upSpeed(self, speed):
        self.speed += speed
        print('현재속도 :',self.speed)
        

class Sedan(Car):
    speed = 10 # 재정의 가능. 있는거 그대로 써도된다. 
    
class Truck(Car):
    pass


c1 = Sedan()
t1 = Truck()


print(c1.speed)
print(c1.color)
c1.upSpeed(80)

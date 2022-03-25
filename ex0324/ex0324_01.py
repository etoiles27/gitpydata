class Car:
    color= 'white'
    speed = 0
    
    def upSpeed(self, speed):
        self.speed += speed
        
    def downSpeed(self,speed):
        self.speed -= speed
    
# 독립객체..
mycar1 = Car()
mycar2 = Car()
mycar3 = Car()

mycar1.color='red'
mycar1.upSpeed(10)
print(mycar1.color,mycar1.speed)

print(mycar2.color,mycar2.speed)
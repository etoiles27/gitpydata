

class Car:
    color ='white'
    
    def __init__(self,color):
        self.color = color
        

c1 = Car('red') # 생성자 호출
c2 = Car('blue')
print(c1.color)
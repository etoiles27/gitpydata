# car 클래스를 만들어서, 
# 변수 color, tire, speed
# 매소드 upSpeed -> 입력받은 속도만큼 증가
#       downSpeed -> 입력받은 속도만큼 감소

# c1 객체 선언 후 
# 색상 red, tire 5개 속도 100 증가, 속도 30감소.
# 색, 타이어개수, 스피드를 출력하세요


class Car:
    color =''
    tire=0
    speed=0
    
    def __init__(self,color,tire):
        self.color = color
        self.tire = tire
    
    def upSpeed(self, speed):
        self.speed += speed
    def downSpeed(self, speed):
        self.speed -= speed
    

c1 = Car('red',5)
c1.upSpeed(100)
c1.downSpeed(30)
print('차의 색상은 :{}, 타이어의 개수는 {}, 차의 속도는 {} 입니다.'.format(c1.color,c1.tire,c1.speed))
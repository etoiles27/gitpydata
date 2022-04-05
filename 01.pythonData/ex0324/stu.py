class Student:
    # 클래스변수 (전역변수)
    # 클래스명.변수명
    stuNo = 0
    # 객체변수 (인스턴스변수)
    stuName = 0
    stuKor = 0
    stuEng = 0
    stuTotal = 0
    stuAvg = 0
    stuRank = 0





    def setKor(self,stuKor):
        if stuKor >= 0:
            self.stuKor = stuKor
            self.total = stuKor+self.stuEng
            self.avg =(stuKor+self.stuEng)/2
        else:
            print("입력값이 잘못되었습니다. ")



    # 생성자
    def __init__(self,stuName,stuKor,stuEng):
        Student.stuNo += 1 # 클래스 변수에서 1 증가해서 자동입력
        # class명.변수 선언을 하면 클래스의 전역변수(글로벌 변수) 선언하는것이 된다. 
        self.stuNo = Student.stuNo
        self.stuName = stuName
        self.stuKor = stuKor
        self.stuEng =stuEng
        self.stuTotal= stuEng+stuKor
        self.stuAvg = (stuEng+stuKor)/2


    # 클래스를 프린트하면 자동으로호출되어 보여주는 함수     
    def __str__(self):
        return '{},{},{}'.format(self.stuNo,self.stuName,self.stuTotal)
    
    if __name__ =='__main__':
        print('현재 자신에서 호출되어 실행함')
        print(stuNo)
    else:
        print('student class 가 호출됨')
    
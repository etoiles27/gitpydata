#from subprocess import STARTUPINFO


class Student:
    stuno = 0
    stuname = ''
    kor = 0
    eng = 0
    total = 0
    avg = 0
    rank = 0 
    
    # class 내 __init__함수로 초기 설정값으로 클래스가 생성됨.
    def __init__(self, stuname='',kor=0,eng=0):
        Student.stuno += 1
        self.stuno = Student.stuno
        self.stuname = stuname
        self.kor = kor 
        self.eng = eng
        self.total = (kor+eng)
        self.avg = (kor+eng)/2
    # 국어 성적을 가져오는 함수     
    def getKor(self):
            return self.kor
    # 국어 성적을 수정하는 함수     
    def setKor(self, kor):
        # 0에서 100 사이의 점수만 입력되게 하는 if문 
        if 0 <= kor <=100:
            # 국어점수가 새롭게 입력되면서, 합계, 평균 모두 업데이트
            self.kor = kor
            self.total = (kor+self.eng)
            self.avg = (kor+self.eng)/2
        else:
            print('입력이 잘못됬습니다. ')
    # 영어 성적을 수정하는 함수          
    def setEng(self, eng):
        # 0에서 100 사이의 점수만 입력되게 하는 if문 
        if 0 <= eng <=100:
            # 영어점수가 새롭게 입력되면서, 합계, 평균 모두 업데이트
            self.eng = eng
            self.total = (self.kor+eng)
            self.avg = (self.kor+eng)/2
        else:
            print('입력이 잘못됬습니다. ')
    
    # rank를 입력받아 클래스에 등수를 입력해주는 함수     
    def setRank(self, rank):
        self.rank = rank
    
    # 총점(합계)을 가져오는 함수
    def getTotal(self):
        return self.total
    
    # 두개의 클래스의 stuname이 같은지를 비교해서 같으면 true 출력
    def __eq__(self, other):
        return self.stuname == other.stuname 
    
    # 현재 클래스의 변수들을 출력
    def __str__(self):
        return '{}\t{}\t{}\t{}\t{}\t{}\t{}\t'.format(self.stuno,self.stuname,self.kor,self.eng,self.total,self.avg,self.rank)
    
        
        
    # def getKor(self):
    #     return self.__kor
    # def setKor(self, kor):
    #     if kor>=0:
    #         self.__kor = kor
    #     else:
    #         print('입력이 잘못됬습니다. ')
    #         # try:
    #         #     raise Exception('입력이 잘못됨')
    #         # except:
    #         #     pass
    # def getEng(self):
    #     return self.__eng
    # def setEng(self, eng):
    #     if eng>=0:
    #         self.__eng = eng
    #     else:
    #         print('입력이 잘못됬습니다. ')
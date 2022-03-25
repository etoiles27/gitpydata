class Student:
    stuno = 0
    stuname = ''
    kor = 0
    eng = 0
    total = 0
    avg = 0
    rank = 0
    
    def __init__(self,stuno,stuname,kor,eng):
        #Student.stuno += 1 
        #self.stuno = Student.stuno
        self.stuno = stuno
        self.stuname = stuname
        self.kor = kor
        self.eng = eng
        self.total = kor+eng
        self.avg = (kor+eng)/2
        
    def setKor(self,kor):
        if kor >= 0:
            self.kor = kor
            self.total = kor+self.eng
            self.avg =(kor+self.eng)/2
        else:
            print("입력값이 잘못되었습니다. ")
    def getKor(self):
        return self.kor
    
    def setStuName(self,stuname):
        tmp=0
        for name in stuname:
            if not stuname.isdigit():
                print('입력이 잘못되었습니다')
                tmp = 1
                break
        if tmp == 0:
            self.stuname = stuname
       
    def __str__(self):
        return '{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(self.stuno,self.stuname,self.kor,self.eng,self.total,self.avg,self.rank)
        




class Student:
    stuNo = 0
    stuName = ''
    stuKor = 0
    stuEng = 0 
    stuTotal = 0
    stuAvg = 0
    stuRank = 0
    
    
    def getStuNo():
        return Student.stuNo
    

    def __init__(self,stuName,stuKor,stuEng):
        Student.stuNo += 1
        self.stuNo = Student.stuNo
        self.stuName = stuName
        self.stuKor = stuKor
        self.stuEng = stuEng
        self.stuTotal = stuKor+stuEng
        self.stuAvg = (stuKor+stuEng)/2
        
    def modifyKor(self,stuKor):
        if 0 <= stuKor <= 100:
            self.stuKor = stuKor
            self.stuTotal = stuKor+self.stuEng
            self.stuAvg =(stuKor+self.stuEng)/2
        else: 
            print('입력이 잘못되었습니다.')   
    
    def modifyEng(self,stuEng):
        if 0 <= stuEng <= 100:
            self.stuEng = stuEng
            self.stuTotal = self.stuKor+stuEng
            self.stuAvg =(self.stuKor+stuEng)/2
        else: 
            print('입력이 잘못되었습니다.')  
            
                
    def __str__(self):
        return '{},{},{}'.format(self.stuNo,self.stuName,self.stuTotal)

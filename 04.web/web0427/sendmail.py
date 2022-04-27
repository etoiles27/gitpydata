
from fileinput import filename
import smtplib
from email.mime.text import MIMEText #MIME 객체
from email.mime.multipart import MIMEMultipart #파일의 내용을 보내는사람,받는사람,내용,파일의 객체를 담기
from email.mime.base import MIMEBase #객체화된 파일을 첨부
from email import encoders #인코딩해줌




def sendEmail(emailadd,tit,cont):
    smtpName = "smtp.naver.com"
    smtpPort = 587
    sendEmail = "rimicom@naver.com"
    password = "gkflagkfla"
    recvEmail = emailadd
    
    title = tit
    content = cont
    msg = MIMEText(content)
    msg['From']=sendEmail
    msg['To']=recvEmail
    msg['subject']=title

    s=smtplib.SMTP(smtpName,smtpPort)
    s.starttls()
    s.login(sendEmail,password)
    s.sendmail(sendEmail,recvEmail,msg.as_string())
    print("메일발송이 완료되었습니다.")
    s.close()
    



def sendEmailWithAttachment(emailadd,tit,cont,filen):
    smtpName = "smtp.naver.com"
    smtpPort = 587
    sendEmail = "rimicom@naver.com"
    password = "1111"
    recvEmail = emailadd
    title = tit
    content = cont
    
    msg = MIMEMultipart('alternative')
    part2 = MIMEText(content)
    msg.attach(part2) #첨부1. 본문의 글자는 따로 attach로 추가
    msg['From'] = sendEmail
    msg['To'] = recvEmail
    msg['Subject'] = title
    part = MIMEBase('application','octet-stream') # application을 하나 만듬

    #파일읽어오기
    with open(filen,"rb") as f:
        part.set_payload(f.read()) #파트라는 app에 read한 파일을 set (part에 파일담기)
        
    #파일을 첨부할 수 있는 형태로 인코딩
    encoders.encode_base64(part)

    #header 정보 정의
    part.add_header('Content-Disposition','attachment',filename=filen)

    #메일 발송
    msg.attach(part) #첨부2. 파일 첨부 추가됨
    s = smtplib.SMTP(smtpName,smtpPort)
    s.starttls()
    s.login(sendEmail,password)
    s.sendmail(sendEmail,recvEmail,msg.as_string())

    print("메일발송이 완료되었습니다.")
    s.close()
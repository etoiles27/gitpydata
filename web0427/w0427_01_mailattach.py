import smtplib #메일발송라이브러리
from email.mime.text import MIMEText # 글자를 보낼 때 사용한다. 


smtpName ="smtp.gmail.com"
smtpPort = 587

sendEmail = 'rimicom1004@gmail.com'
password = 'unjmkgprcgwddsnm'
recvEmail = sendEmail
# recvEmail = 'xnmx1234@naver.com'

title = '[test] in calss  - sending gmail'
content ='contents - 냉무'

msg = MIMEText(content)
msg['From']=sendEmail
msg['To']=recvEmail
msg['subject']=title

s=smtplib.SMTP(smtpName,smtpPort)
s.starttls()
s.login(sendEmail,password)
s.sendmail(sendEmail,recvEmail,msg.as_string())
s.close()
import smtplib
from email.mime.text import MIMEText
from email.header import Header



s = smtplib.SMTP("smtp.163.com",25)
mail_user = "13675606386@163.com"
mail_pass = "Zyzx1314"
smtp.login(mail_user,mail_pass)
content = '本次测试通过率为99%'
Subject = "2019-12-19测试报告"
From = '751917330@qq.com'
To = "测试人"
message = MIMEText(content,'plain','utf-8')
message['Subject'] = Header(Subject,'utf-8')
message['From'] = From
message['To'] = To
smtp.send_message(msg=msg,from_addr="751917330@qq.com",to_addrs="13675606386@163.com")

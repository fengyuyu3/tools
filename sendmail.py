from email.mime.text import MIMEText
from email.utils import formataddr
import smtplib

def send_mail():
    try:
        my_sender = 'fanliqi724@163.com' #发件人邮箱账号，为了后面易于维护，所以写成了变量
        my_user = 'fanliqi@bestwise.cc' #收件人邮箱账号，为了后面易于维护，所以写成了变量
        msg = MIMEText('测试', 'plain', 'utf-8')
        msg['From'] = formataddr(["test发件人", my_sender])  #括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To'] = formataddr(["test收件人", my_user])  #括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject'] = "主题" #邮件的主题，也可以说是标题

        server=smtplib.SMTP("smtp.163.com", 25) #发件人邮箱中的SMTP服务器，端口是25
        server.login(my_sender, "xxxxx")  #括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender, [my_user, ], msg.as_string())  #括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  #这句是关闭连接的意思
    except Exception :
        print("发送失败 "+str(Exception))

if __name__ == "__main__":
    send_mail()
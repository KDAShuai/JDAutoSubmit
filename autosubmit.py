form email.mime.text import MIMEText
import smtplib


# 发送提醒邮件
def send_ReminderEmail(good_name):
    mail_host = 'smtp.qq.com'
    mail_user = ''
    mail_psw = ''
    mail_postfix = 'qq.com'
    me = mail_user + '<' + mail_user + '@' + mail_postfix + '>'
    msg = MIMEText('Congratulations!\r\nYour good:\r\n' + good_name + '\r\nis submitted in JD successfully!\r\nPlease check and pay for it!')
    msg['Subject'] = 'Successfully Snapped Up Good'
    msg['From'] = me
    msg['To'] = ''
    try:
        s = smtplib.SMTP()
        s.connect(mail_host)
        s.login(mail_user, mail_psw)
        s.sendmail(me, me, msg.as_string())
        s.close()
        return True
    except Exception, e:
        print(str(e))
        return False

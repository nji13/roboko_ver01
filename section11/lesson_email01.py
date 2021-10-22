# email送信  hotmailの手順は以下になる。gmailなどその他のメールの場合はポートが違ったり等、手順が違う場合がある。

from email import message
import smtplib


smtp_host = 'smtp.live.com'
smtp_port = 587
from_email = 'jetfield@hotmail.co.jp'
to_email = 'jetfield@hotmail.co.jp'
username = 'jetfield@hotmail.co.jp'
password = 'crea1021'

msg = message.EmailMessage()
msg.set_content('Test email')
msg['Subject'] = 'Test email sub'
msg['From'] = from_email
msg['To'] = to_email

server =smtplib.SMTP(smtp_host, smtp_port)
server.ehlo()
server.starttls()
server.ehlo()
server.login(username, password)
server.send_message(msg)
server.quit()
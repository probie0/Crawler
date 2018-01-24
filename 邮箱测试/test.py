import smtplib
from email.mime.text import MIMEText
account = "2372247434@qq.com"
pwd  = "eqkxqivhzoaxdied"
_to   = "1401253567@qq.com"

msg = MIMEText("Test")
msg["Subject"] = "don't panic"
msg["From"]    = account
msg["To"]      = _to


s = smtplib.SMTP_SSL("smtp.qq.com", 465)
s.login(account, pwd)
s.sendmail(account, _to, msg.as_string())
s.quit()
print("Success!")

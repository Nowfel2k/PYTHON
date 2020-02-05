import smtplib
from email.mime.text import MIMEText

try:
    body = "Email send from Python Program. Hello Nibba."

    def sendEmail(to, content):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('muhammednavfal1@gmail.com', 'Abdullah0')
        server.sendmail('muhammednavfal1@gmail.com', to, content)
        server.close()

    msg = MIMEText(body)
    msg['From'] = "muhammednavfal1@gmail.com"
    msg['To'] = 'muhammednavfal1@gmail.com'
    msg['Subject'] = 'Test1'

    content = msg
    to = "muhammednavfal1@gmail.com"
    sendEmail(to, content)

except Exception as e:
    print(e)

else:
    print("\nEmail Sent Successfully.")



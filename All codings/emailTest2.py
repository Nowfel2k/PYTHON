import smtplib
try:
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("muhammednavfal1@gmail.com", "Abdullah0")
    message = "Hello"
    s.sendmail("muhammednavfal1@gmail.com", "muhammednavfal1@gmail.com", message)
    s.quit()
except exception as e:
    print(e)
else:
    print("Email sent successfully!")

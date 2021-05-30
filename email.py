import ssl , smtplib
port = 465
email = input('Email Address: ')
password = input('Password: ')
recipient = input('Enter the recipient Email Address: ')
subject = input('Enter Subject : ')
text = input ('Type your Message:')
message = 'Subject: {}\n\n{}'.format(subject,text)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', port,context = context) as servers:
    server.login(email,password)
    server.sendmail(email,recipient,message)

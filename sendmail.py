import smtplib
s=smtplib.SMTP("smtp.gmail.com",587)
s.starttls()
s.login("awesome.assassin01@gmail.com","insane@2003")
message=("everthing is working fine!!")
s.sendmail("awesome.asssassin01@gmail.com","atullsharma2000@gmail.com",message)
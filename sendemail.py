import smtplib

fromaddr = 'adrene.mcintosh@gmail.com'

toaddr  = ['adrene.mcintosh6@gmail.com']

#message = """From: {} <{adrene.mcintosh@gmail.com}>

#To: {To Person} <{adrene.com}>

#Subject: {SMTP e-mail test}

#{}"""
message = """I open at the close"""
Subject = "1995"
messagetosend = message.format(
                             fromaddr,


                             toaddr,


                             message)

# Credentials (if needed)

username = 'adrene.mcintosh@gmail.com'

password = 'dftl wygs flkc zlfg'


# Prepare actual message

message = """\
fromaddr: %s
toaddr: %s
messagetosend: %s
%s
""" % (fromaddr, ", ".join(toaddr), messagetosend, Subject)

# Send the mail

# The actual mail send

server = smtplib.SMTP('smtp.gmail.com:587')

server.starttls()

server.login(username,password)

server.sendmail(fromaddr, toaddr, messagetosend)

server.quit()

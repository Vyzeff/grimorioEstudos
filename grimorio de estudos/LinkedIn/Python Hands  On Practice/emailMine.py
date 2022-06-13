import smtplib
#SERVER = "localhost"


def sendEmail(sender, receiver, subject, text):
    smtp_obj = smtplib.SMTP("smtp.gmail.com", 587)
    smtp_obj.ehlo()

    smtp_obj.starttls() #setting up to TLS connection
    smtp_obj.ehlo() #calling the ehlo() again as encryption happens on calling startttls()

    smtp_obj.login(sender, "852316497asd123") #logging into out email id

    smtp_obj.sendmail(sender,receiver, msg=text)
    print("Email sent!")

    smtp_obj.quit()#terminating the server

if __name__ =="__main__":
    TO = list(input("To whom the email is: "))
    FROM = input("From who: ")
    SUBJECT = input("Subject: ")
    TEXT = input("Body of text:")
    
    sendEmail(FROM, TO, SUBJECT, TEXT)
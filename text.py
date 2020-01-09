import smtplib
def notify(emailid, number, className, url):
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login('rucoursesearcher@gmail.com', 'PASSWORD();') # Delete this line!
        subject = "A class has opened up!"
        body = "The class "+ className + " has just opened up. Register quick at "+url
        message = f'Subject: {subject}\n\n{body}'

        smtp.sendmail('rucoursesearcher@gmail.com', str(number)+"@tmomail.net", message)
        smtp.sendmail('rucoursesearcher@gmail.com', str(number)+"@txt.att.net", message)
        smtp.sendmail('rucoursesearcher@gmail.com', str(number)+"@vzwpix.com", message)
        smtp.sendmail('rucoursesearcher@gmail.com', str(number)+"@messaging.sprintpcs.com", message)
        smtp.sendmail('rucoursesearcher@gmail.com', emailid, message)




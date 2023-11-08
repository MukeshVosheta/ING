from email.message import EmailMessage
import random
import ssl
import smtplib

#________________________OTP generator and varification____________________________
def otp_varify(reciver_mail):
    e_send="sun"
    e_pass="onhgjwzm"
    e_reci=reciver_mail
    otp=random.randint(100000,999999)

    sub="Dont'share"
    body=f''' InnoveGallery 

    Your registeration 6 digit OTP is : {otp}
    '''

    es=EmailMessage()

    es['FROM']=e_send
    es['TO']=e_reci
    es['SUBJECT']=sub

    es.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465,context=context) as smtp:
        smtp.login(e_send,e_pass)
        smtp.sendmail(e_send,e_reci,es.as_string())
    
    data=[e_reci,otp]

    return data

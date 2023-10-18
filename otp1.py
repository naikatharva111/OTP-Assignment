import math
import random
import smtplib
from twilio.rest import Client
account_sid = 'ACc90b01dc3b9e5727a207731cb591b9a7'
auth_token = '4e9aaa48cbdd9aac7dc4a1f7a6c09c99'
twilio_number = '+15856394364'
# Generate OTP
def GenerateOTP():
    digits = "0123456789"
    length = len(digits)
    otp = ""

    for i in range(6):
        otp += digits[math.floor(random.random()*length)]

    return otp




# validate the mobile number
def ValidateMobile(PhoneNo):
     if len(PhoneNo) != 10:
       
        return False
     else:
         return True 




#validate the emailid
def ValidateEmailID(Email):
    if "@gmail.com" not in Email:
    
        return False
    else:
        return True




# send OTP to input mobile number
def sendOTPOverMobile(PhoneNo2, OTP):
    client = Client(account_sid, auth_token)
    Message = client.messages.create(
        body="Your 6 digit OTP is "+OTP,

        from_=twilio_number,
        to='+91'+str(PhoneNo2),
    )
    print(Message.body)




# send OTP to input emailid
def sendOTPOverEmail(Email2, OTP):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()  
    server.login('naikatharva111@gmail.com', 'jbctzddvhpwysdhf')
    message = 'Your 6 digit OTP is '+str(OTP)
    server.sendmail('naikatharva111@gmail.com',
                    Email2, message)
    server.quit()





PhoneNo = input("Enter the number:")
Email = input("Enter the Email:")
if(ValidateMobile(PhoneNo)):
    PhoneNo2 = PhoneNo
else:
    PhoneNo2 = input("enter a valid mobile number")    


if(ValidateEmailID(Email)):
    Email2 = Email
else:
    Email2 = input("enter the valid email")




OTP = GenerateOTP()

sendOTPOverMobile(PhoneNo2, OTP)

sendOTPOverEmail(Email2, OTP)






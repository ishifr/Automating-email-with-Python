# ready
import smtplib
import os
import imghdr
from email.message import EmailMessage

count = int(input("How many names you would like to enter:"))
f=open("mydoc.xlsx", "a+")
for i in range(count):
    me = input("Enter a name:")
    f.write(str(i+1) +" - "+ me + '\n')
f.close()

email_id = "" #sender's email address
email_pass = "" #sender's email password

msg = EmailMessage()
msg["Subject"] = "Check out our Pic"
msg["From"] = email_id
msg["To"] = "" # => write here reciver's email address 
msg.set_content("Is that good or not")

with open("mydoc.xlsx", "rb") as m: 
    file_data = m.read()
    file_name = m.name

msg.add_attachment(file_data, maintype = "image", subtype="octet-stream", filename= file_name)

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:  # 587 is port number
    smtp.login(email_id,email_pass)   
    smtp.send_message(msg)
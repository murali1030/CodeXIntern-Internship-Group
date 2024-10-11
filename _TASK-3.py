#!/usr/bin/env python
# coding: utf-8

# # TASK-3

# 5. Command-Line E-Mail Sender:
# A script that sends emails using SMTP, possibly with attachments.

# In[1]:


import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


# In[2]:


def send_email(sender_email, sender_password, recipient_email, subject, message):
   try: 
        
       msg = MIMEMultipart()
       msg['From'] = sender_email
       msg['To'] = recipient_email
       msg['Subject'] = subject

  
       msg.attach(MIMEText(message, 'plain'))

        
       server = smtplib.SMTP('smtp.gmail.com', 587)
       server.starttls() 
       server.login(sender_email, sender_password)  

       text = msg.as_string()
       server.sendmail(sender_email, recipient_email, text)

       print(f"Email sent successfully to {recipient_email}")
       server.quit()  
   except Exception as e:
       print(f"Failed to send email. Error: {e}")

if __name__ == "__main__":
   sender_email = input("Enter your email: ")
   sender_password = input("Enter your password: ")
   recipient_email = input("Enter recipient email: ")
   subject = input("Enter subject: ")
   message = input("Enter your message: ")

   send_email(sender_email, sender_password, recipient_email, subject, message)


# In[ ]:





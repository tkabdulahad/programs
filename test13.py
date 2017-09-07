#!/usr/bin/python3
import smtplib
s=smtplib.SMTP('smtp.gmail.com',587)
s.starttls()
s.login("tkabdulahad123@gmail.com","456abdulahad")
message="hello. how are you"
s.sendmail("tkabdulahad123@gmail.com","tkabdulahad123@gmail.com",message)
s.quit()
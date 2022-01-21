import re
import socket
import os
import sys
import json


s = socket.socket()
print("Socket successfully created")
port =8080
s.bind (('',port))
print("socket binded to " +str(port))
s.listen(5)
print("socket is listening")
while True:
c, addr =s.accept()
print(Got connection from" + str(addr))

c.send("Welcome to Quiz History")
jawapan= input ("Are you ready?(YES/NO) ")
markah=0
Mark=0
jumlah=5
if jawapan.upper()=='YES':
#Soalan1
c.send("Question 1:What Year do Portuguese attack Malacca?(1952/1511/1841)? ")
if answer.lower()=='1511':
markah+=1
c.send("Correct answer ")
else:
c.send("Wrong answer. Correct answer is 1511")
#Soalan2
c.send ("Question 2:In between 8 December 1941 Japanese invented Malaya, Where do first Japanese lay down? Malacca/Penang/Kelantan ")
if answer.lower()=='Penang':
markah+=1
c.send("Correct answer ")
else:
c.send("Wrong answer. Correct answer is Penang")
#Soalan3
c.send ("Question 3:What year do Singapore separated from Malaysia?(1957/1988/1965) ")
if answer.lower()=='1965':
markah+=1
c.send("Correct answer ")
else:
c.send("Wrong answer. Correct answer is 1965")
#Soalan4
c.send ("Question 4:Year Malaysia  independent?(1988/1880/1957) ")
if answer.lower()=='1957':
markah+=1
c,send("Correct answer ")
else:
c.send("Wrong answer. Correct answer is 1957")
#Soaln5
c.send ("Question 5:When do Malaysia have currency itself?(1967/1955/1952) ")
if answer.lower()=='1967':
markah+=1
c.send("Correct answer ")
else:
c.send("Wrong answer. Correct answer is 1967")
c.send ("Thank you for play your answer ", markah,"question" )
mark=(markah/jumlah)*100
c.send ("Mark for you",mark)
c.send("See you next time")

c.close()

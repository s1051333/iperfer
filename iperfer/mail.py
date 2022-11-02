import socket

mailServer = 'smtp.mailtrap.io'
mailPort = 2525
endmsg = "\r\n.\r\n"

#creat socket and tcp connection 
clientSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
clientSocket.connect((mailServer,mailPort)) 
recv = clientSocket.recv(1024)
print(recv.decode())

# Send EHLO command and print server response.
command = f'EHLO {mailServer}\r\n'
clientSocket.send(command.encode())
recv1 = clientSocket.recv(1024)
print(recv1.decode())


AUTH = "AUTH LOGIN\r\n"
clientSocket.send(AUTH.encode())
recv6 = clientSocket.recv(1024)
print(recv6.decode())

AUTH = "YmVkODdmMTE2NDA1Njk\r\n"
clientSocket.send(AUTH.encode())
recv7 = clientSocket.recv(1024)
print(recv7.decode())

AUTH = "YWRjMjZkNGZkNjg2Njc\r\n"
clientSocket.send(AUTH.encode())
recv8 = clientSocket.recv(1024)
print(recv8.decode())



# Send MAIL FROM command and print server response.
mailFrom = f"MAIL FROM: <aqsw210160@gmail.com> \r\n"
clientSocket.send(mailFrom.encode())
recv2 = clientSocket.recv(1024)
print(recv2.decode())


# Send RCPT TO command and print server response.
rcptTo = "RCPT TO: <aqsw210160@gmail.com> \r\n"
clientSocket.send(rcptTo.encode())
recv3 = clientSocket.recv(1024)
print(recv3.decode())


# Send DATA command and print server response.
data = "DATA\r\n"
clientSocket.send(data.encode())
recv4 = clientSocket.recv(1024)
print(recv4.decode())


# Send message data.
subject = "Subject: SMTP mail client testing \r\n\r\n" 
clientSocket.send(subject.encode())
recipient = input("recipient’s email address: ")
message = input("message context :")
all_message = f"""To: {recipient}
From: aqsw210160@gmail.com
Subject: {message}"""
clientSocket.send(all_message.encode())
clientSocket.send(endmsg.encode())
recv5 = clientSocket.recv(1024)
print(recv5.decode())


# Send QUIT command and get server response.
clientSocket.send("QUIT\r\n".encode())
message=clientSocket.recv(1024)
clientSocket.close()
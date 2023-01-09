import zmq
import constPS #-
import threading
import rpyc
import sys
from socket  import *
import pickle

my_ip = ""
name = ""

def login():
  global name
  name = input("Enter your name: ")
  answear = conn.root.exposed_finduser(name)
  if answear == "Found":
    password = input("Enter your password: ")
    answear = conn.root.exposed_validatepassword(name, password)
    if answear == "Wrong":
      print("WRONG PASSWORD! THE PROGRAM IS EXITING!")
      sys.exit()
    print("WELCOME: ", name)
  else:
    my_ip = input("Enter your IP: ")
    password = input("Enter your password: ")
    answear = conn.root.exposed_crateuser(name, password, my_ip)
    if answear == "Done":
      print("Successfully registered!\nWelcome: ", name)
    else:
      print("Could not register your user!\nTry again later!\n")
      sys.exit()

class RecvHandler(threading.Thread):
  def __init__(self, sock):
    threading.Thread.__init__(self)
    self.client_socket = sock
    self.daemon=True

  def run(self):
    while True:
        (conn, addr) = self.client_socket.accept() 
        marshaled_msg_pack = conn.recv(1024)   
        msg_pack = pickle.loads(marshaled_msg_pack) 
        print("\n\nYou got a new direct message!\nMESSAGE: " + msg_pack[0] + " - FROM: " + msg_pack[1] + '\n')
        conn.close()
        return

class SubscriberHandler(threading.Thread):
  def __init__(self):
    threading.Thread.__init__(self)
    self.daemon=True

  def run(self):
      while True:  
        message = s.recv()   # receive a message
        print (bytes.decode(message))

# Connects to RPC
conn = rpyc.connect(constPS.HOST, constPS.PORT_RPYC)
# Login
login()
# socket direct message
client_sock = socket(AF_INET, SOCK_STREAM) # socket for server to connect to this client
client_sock.bind((my_ip, 5680))
client_sock.listen(5)
recv_handler = RecvHandler(client_sock)
recv_handler.start()
# Connects to ZEROMQ
context = zmq.Context()
s = context.socket(zmq.SUB)         
p = "tcp://"+ constPS.HOST +":"+ constPS.PORT_ZEROMQ        
s.connect(p)                         
print("Choose the topics that you want to subscribe: \nThe following topics are available: ")
for item in constPS.registry_topics:
  print(item, end=" ")
print("\n")
topics = input("Enter all topics you want to subscribe to on the same line and separated by a space: ").split()
for item in topics:
  s.setsockopt_string(zmq.SUBSCRIBE, item)  # subscribe to TIME messages
# Creates ZEROMQ thread
subscriber_thread = SubscriberHandler()
subscriber_thread.start()
menu = input("Choose the option that best fit your needs: \n1 - Send a group message. \n2 - Send a message to a user\n")
while menu != 0:
    if (menu == "1"):
      topic = input("Enter the topic: ")
      message = input("Enter the message: ")
      conn.root.exposed_publish(topic, message)
    if(menu == "2"):
      user = input("Enter the user you want to send your message to: ")
      answear = conn.root.exposed_finduser(user)
      if answear == "User not found!":
        print(answear, "\n")
      message = input("Enter your message: ")
      answear = conn.root.exposed_sendmessage(name, user, message)
      if answear == "Error":
        print("An error ocurred!\nTry again later!\n")
      else:
        print("Your message was sent!\n")
    elif(menu == "0"):
      print("\nGoodbye! Hope to see you again!\n")
      sys.exit()
    else:
      print("Could not understand!\nPlease try again!\n")
    menu = input()
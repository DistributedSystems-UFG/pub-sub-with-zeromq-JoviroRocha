import zmq
import constPS #-
import threading
import rpyc

class SubscriberHandler(threading.Thread):
  def __init__(self):
    threading.Thread.__init__(self)

  def run(self):
      while True:  
        message = s.recv()
        print (bytes.decode(message))

context = zmq.Context()
s = context.socket(zmq.SUB)          # create a subscriber socket
p = "tcp://"+ constPS.HOST +":"+ constPS.PORT_ZEROMQ        # how and where to communicate
s.connect(p)                         # connect to the server
print("Choose the topics that you want to subscribe: \nThe following topics are available: ")
for item in constPS.registry_topics:
  print(item)
topics = input("Enter all topics you want to subscribe to on the same line and separated by a space: ").split()
for item in topics:
  print(item)
  s.setsockopt_string(zmq.SUBSCRIBE, item)  # subscribe to TIME messages
    
subscriber_thread = SubscriberHandler()
subscriber_thread.start()
conn = rpyc.connect(constPS.HOST, constPS.PORT_RPYC)
while True:
    topic = input("Enter the topic: ")
    message = input("Enter the message: ")
    conn.root.exposed_publish(topic, message)
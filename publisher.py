import zmq, time
import constPS  #-

context = zmq.Context()
s = context.socket(zmq.PUB)        # create a publisher socket
p = "tcp://"+ constPS.HOST +":"+ constPS.PORT      # how and where to communicate
s.bind(p)                          # bind socket to the address
while True:
	topic = input("Enter the topic that you want to send your message: ")
	message = input("Enter your message: ")
	msg = str.encode(topic + " " + message)
	s.send(msg) # publish the current time

import zmq
import constPS #-

context = zmq.Context()
s = context.socket(zmq.SUB)          # create a subscriber socket
p = "tcp://"+ constPS.HOST +":"+ constPS.PORT        # how and where to communicate
s.connect(p)                         # connect to the server
print("Choose the topics that you want to subscribe: \nThe following topics are available: ")
for item in constPS.registry_topics:
	print(item)
topics = input("Enter all topics you want to subscribe to on the same line and separated by a space: ").split()
for item in topics:
	s.setsockopt_string(zmq.SUBSCRIBE, item)  # subscribe to TIME messages

while True:
	message = s.recv()   # receive a message
	print (bytes.decode(message))

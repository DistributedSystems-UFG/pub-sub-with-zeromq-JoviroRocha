import zmq, time
import constPS  #-
import threading
import rpyc
from rpyc.utils.server import ThreadedServer

def exposed_publish(self, topic, message):
	context = zmq.Context()
    s = context.socket(zmq.PUB)        # create a publisher socket
    p = "tcp://"+ constPS.HOST +":"+ constPS.PORT      # how and where to communicate
    s.bind(p)        
    msg = str.encode(topic + " " + message)
	s.send(msg) # publish the current time 
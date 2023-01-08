import zmq, time
import constPS  #-
import threading
import rpyc
from rpyc.utils.server import ThreadedServer

class Chating(rpyc.Service):
    def exposed_publish(self, topic, message):      
        msg = str.encode(topic + " " + message)
        s.send(msg) # publish the current time
   
if __name__ == "__main__":
    context = zmq.Context()
    s = context.socket(zmq.PUB)        # create a publisher socket
    p = "tcp://"+ constPS.HOST +":"+ constPS.PORT_ZEROMQ      # how and where to communicate
    s.bind(p)
    server = ThreadedServer(Chating(), port = constPS.PORT_RPYC)
    server.start()
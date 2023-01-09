import zmq, time
import constPS  
import rpyc
from rpyc.utils.server import ThreadedServer
import json
from socket  import *
import pickle

class Chating(rpyc.Service):

    def exposed_publish(self, topic, message):      
        msg = str.encode( topic + " - " + message)
        s.send(msg) # publish the current time
    
    def exposed_finduser(self, name):
        f = open(constPS.filename)
        data = json.load(f)
        if name in data:
            f.close()
            return "Found"
        else:
            f.close()
            return "Not Found"
    
    def exposed_validatepassword(self, name, password):
        f = open(constPS.filename)
        data = json.load(f)
        if data[name][1] == password:
            f.close()
            return "Correct"
        else:
            f.close()
            return "Wrong"
    
    def exposed_crateuser(self, name, password, ip):
        user = {name: [ ip, password ]}
        with open(constPS.filename, "r") as file:
            data = json.load(file)
        data.update(user)
        with open(constPS.filename, "w") as file:
            json.dump(data, file)
        return "Done"
    
    def exposed_sendmessage(self, name, user, message):
        f = open(constPS.filename)
        data = json.load(f)
        ip = data[user][0]
        client_sock = socket(AF_INET, SOCK_STREAM)
        try:
            client_sock.connect((ip, 5680))
        except error:
            print(error)
            return "Error"
        msg_pack = (message, name)
        marshaled_msg_pack = pickle.dumps(msg_pack)
        client_sock.send(marshaled_msg_pack)
        return        
        
if __name__ == "__main__":
    context = zmq.Context()
    s = context.socket(zmq.PUB)        # create a publisher socket
    p = "tcp://"+ constPS.HOST +":"+ constPS.PORT_ZEROMQ      # how and where to communicate
    s.bind(p)
    server = ThreadedServer(Chating(), port = constPS.PORT_RPYC)
    server.start()
import zmq
import time
import threading

# ZeroMQ Context
context = zmq.Context()

# Define the socket using the "Context"
sock = context.socket(zmq.PUB)
sock1 = context.socket(zmq.REP)
sock.bind("tcp://127.0.0.1:5680")
sock1.bind("tcp://127.0.0.1:5677")
try:
    while True:
        mess = sock1.recv_string()
        sock1.send_string("")
        messages = mess.split(" ",1)
        try:
            sock.send_string("["+messages[0]+"] : "+messages[1])
        except IndexError:
            print("Invalid arguments")
            exit(0)
except KeyboardInterrupt:
    print("Disconnected!")
    exit(0)
import zmq
import threading
import sys

# ZeroMQ Context
context = zmq.Context()

# Define the socket using the "Context"
sock = context.socket(zmq.SUB)
sock1 = context.socket(zmq.REQ)

# Define subscription and messages with prefix to accept.
sock.setsockopt_string(zmq.SUBSCRIBE, "")
sock.connect("tcp://127.0.0.1:5680")
sock1.connect("tcp://127.0.0.1:5677")

try:
    name = sys.argv[1]
except IndexError:
    print("Please enter the username, exiting...")
    exit(0)

def out_thread():
    CURSOR_UP_ONE = '\x1b[1A'
    ERASE_LINE = '\x1b[2K'
    print("User [%s] connected to the chat server" % name)
    print("[%s] > " % name)
    while True:
        s = input()
        sys.stdout.write(CURSOR_UP_ONE + ERASE_LINE)
        sock1.send_string(name+" "+s)
        mess = sock1.recv_string()

def in_thread():
    CURSOR_UP_ONE = '\x1b[1A'
    ERASE_LINE = '\x1b[2K'
    while True:
        message = sock.recv_string()
        print(message)

thread1 = threading.Thread(target=out_thread)
thread2 = threading.Thread(target=in_thread)

thread1.start()
thread2.start()




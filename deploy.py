import socket
import subprocess 
import os

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('', 1337)

sock.bind(server_address)

sock.listen(1)

prevProc = None

while True:
    print "LISTENING"
    connection, client_address = sock.accept()
    connection.recv(1024)
    if prevProc != None:
        prevProc.terminate()
    print "DEPLOYING"
    print os.getcwd()
    # os.system('git add .')
    # os.system('git commit -m \"Server Update\"')
    # os.system('git pull origin master')
    # os.system('git push origin master')

    # prevProc = subprocess.Popen(['git commit -am "Server update"'])
    # prevProc = subprocess.Popen(['git','pull','origin','master'])
    # prevProc = subprocess.Popen(['git','push','origin','master'])
    # prevProc = subprocess.Popen(['java', '-jar', 'server.jar'])

    prevProc = subprocess.Popen([os.path.join(os.getcwd(), 'run.cmd')])

    connection.close()


    


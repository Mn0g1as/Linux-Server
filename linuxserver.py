import socket

ip = "192.168.1.X"
port = 4444

def main():
  sock = socket.socket(socket.AF_INET,
                       socket.SOCK_STREAM)
  adress = (ip, port)
  sock.bind(address)
  sock.listen(1)
  print("put the port: " + str(port))
  conn , ipvictim = sock.accept()
  msg = "This is an Message :D"
  conn.send(msg.endcode())
  conn.close()

main()


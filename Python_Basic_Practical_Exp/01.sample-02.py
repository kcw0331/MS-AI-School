# IP Address
from os import lseek
import socket

in_addr = socket.gethostbyname(socket.gethostname())

print(in_addr)
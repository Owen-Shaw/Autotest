import socket
import time
import serial

def Screenshot(serial):
    serial.write(b'screencap -p /data/UARTSmartMonkey.png\n')
    print("Screenshot Success")
    time.sleep(10)
    LocalIp = get_local_ip()
    command = "busybox ftpput {ip}:8065 UARTSmartMonkey.png /data/UARTSmartMonkey.png\n".format(ip=LocalIp)
    bytes_command = command.encode("utf-8")
    serial.write(bytes_command)
    print("FTPPUT Success")
    time.sleep(10)


def get_local_ip():
    ip = socket.gethostbyname(socket.gethostname())
    return ip
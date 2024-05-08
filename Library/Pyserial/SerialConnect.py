import serial

def SerialOpen(Port = "com3",Baudrate = 115200,Timeout = 0.5):
    # 配置串口
    Serial = serial.Serial(
        port=Port,  # 串口名称
        baudrate=Baudrate,  # 波特率
        bytesize=serial.EIGHTBITS,  # 数据位
        parity=serial.PARITY_NONE,  # 校验位
        stopbits=serial.STOPBITS_ONE,  # 停止位
        timeout=Timeout  # 超时时间
    )
    if Serial.isOpen():
        print(Serial.port,"open Serial success ; baudrate =",Serial.baudrate)
        print("-" * 160)
    else:
        print(Serial.port,"open Serial failed!!!")
        print("-" * 160)
    return Serial
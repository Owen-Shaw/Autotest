from Library.Pyserial import SerialConnect


def TVcontrol():
    serial = SerialConnect.SerialOpen(Port="com3", Baudrate=115200)
    serial.write(b'am start -S -W com.changhong.mmp.fileexplorer/com.changhong.mmp.fileexplorer.ChangHongFileExplorerActivity\n')


if __name__ == '__main__':
    TVcontrol()
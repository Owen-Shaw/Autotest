from Library.Pyserial import SerialConnect
from Library.OpenCV import ImageContrast


def TVcontrol():
    serial = SerialConnect.SerialOpen(Port="com3", Baudrate=115200)
    serial.write(b'am start -S -W com.changhong.mmp.fileexplorer/com.changhong.mmp.fileexplorer.ChangHongFileExplorerActivity\n')


if __name__ == '__main__':
    # 对比图像
    image1 = "/Users/owenshaw/Documents/Git/Autotest/1.JPG"
    image2 = "/Users/owenshaw/Documents/Git/Autotest/2.aJPG"
    result = ImageContrast.Contrast(image1, image2)
    baseline = 0.99
    print(result)
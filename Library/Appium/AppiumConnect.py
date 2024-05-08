# 配置Appium
import json
from appium import webdriver

def Connect(CapabilitySetsPath):
    # 读取手机CapabilitySets信息
    with open(CapabilitySetsPath, "r", encoding="utf-8") as f:
        caps = json.load(f)
    return caps

def GetDriver(caps):
    # 连接手机
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', caps)
    print("Appium Connect Success")
    print("-" * 160)
    return driver

if __name__ == '__main__':
    caps =Connect()
    print(caps)


import os
import time
import warnings
import sys


def stop_appium(post_num=4723,pc="WIN"):
    '''关闭appium服务'''
    if pc.upper() =='WIN':
        os.system('chcp 65001')
        p = os.popen(f'netstat -aon|findstr {post_num}')
        p0 = p.read().strip()
        if p0 != '' and 'LISTENING' in p0:
            p1 = int(p0.split('LISTENING')[1].strip()[0:5])  # 获取进程号
            os.popen(f'taskkill /F /PID {p1}')  # 结束进程
        # os.popen(f'taskkill /F /IM cmd.exe')  # 结束进程
        os.system(f'taskkill /F /IM cmd.exe')
        print('appium server已结束')
        print("-" * 160)
    elif pc.upper() == 'MAC':
        p = os.popen(f'lsof -i tcp:{post_num}')
        p0 = p.read()
        if p0.strip() != '':
            p1 = int(p0.split('\n')[1].split()[1])  # 获取进程号
            os.popen(f'kill {p1}')  # 结束进程
            print('appium server已结束')

def start_appium(post_num=4723,pc="WIN"):
    '''开启appium服务'''
    stop_appium(post_num)    # 先判断端口是否被占用，如果被占用则关闭该端口号
    # 根据系统，启动对应的服务
    cmd_dict = {
        'WIN':f'start appium -a 127.0.0.1 -p {post_num} ',
        'MAC':f'appium -a 127.0.0.1 -p {post_num} --log xxx.log --local-timezone  & '
    }
    os.system(cmd_dict[pc.upper()])
    time.sleep(3)  # 等待启动完成
    print('appium server启动成功')
    print("-" * 160)

if __name__ == '__main__':
    start_appium()

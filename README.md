# Autotest

1、Library能力库层，放置Appium、Selenium、Pyserial、opencv等能力库

2、Script脚本层，标准的Python unittest测试用例，向下调用Library能力库，支持PyCharm的单用例调试执行

3、Runner执行层，提供本地多用例的执行，GUI界面调度执行，Jenkins调度执行，以及报告生成。


conda install pytest

pip install Appium-Python-Client

conda install pyserial

pip install numpy 

pip install matplotlib

pip install opencv-python
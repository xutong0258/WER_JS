import pyautogui
import subprocess
import time
import os

# 启动 WhatsApp
os.startfile(r"D:\电脑管家迁移文件\windADK\Assessment and Deployment Kit\Windows Assessment Toolkit\x86\wac.exe")
# 或者 wac.exe
# subprocess.Popen(r"C:\Users\%USERNAME%\AppData\Local\WhatsApp\wac.exe")

print("等待 WhatsApp 启动...")
time.sleep(10)

# 确保窗口最大化或激活
pyautogui.hotkey('win', 'up')  # 最大化当前窗口
time.sleep(1)


# 示例：点击搜索框（提前截图保存为 search_box.png）
# pyautogui.click(pyautogui.locateCenterOnScreen('search_box.png', confidence=0.8))

# 直接写坐标（最快，但屏幕分辨率/缩放改变会失效）
def auto_send():
    # 点击搜索框（坐标根据你屏幕自己调）
    pyautogui.click(200, 120)
    time.sleep(1)
    pyautogui.write('张三', interval=0.1)
    time.sleep(1.5)
    pyautogui.click(200, 250)  # 点击搜索结果第一条

    time.sleep(2)
    pyautogui.click(700, 980)  # 点击消息输入框
    pyautogui.write('Python 自动发消息成功！', interval=0.05)
    time.sleep(0.5)
    pyautogui.press('enter')


auto_send()
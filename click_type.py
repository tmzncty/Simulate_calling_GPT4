import pyautogui
import keyboard
import time
from pynput.keyboard import Controller, Key

def paste_and_enter():
    #连CTRL+C都懒得按下的懒人
    #pyautogui.hotkey('ctrl', 'c')
    # 点击指定坐标，使对话框获得焦点
    # 请将下面的x和y替换为您刚才获取到的坐标值
    x = 725
    y = -105
    # 将光标移动到对话框上
    pyautogui.moveTo(x, y)

    # 点击对话框以聚焦
    pyautogui.click()

    # 等待一段时间，确保对话框已聚焦
    time.sleep(1)
    keyboard = Controller()
    #请自己添加问题
    #text_to_input = "请帮我润色下面这段话"
    #pyautogui.write("请帮我润色下面这段话")
    #time.sleep(1)
    # 输入文本
    text_to_type = "请帮我润色下面这段话"

    # 等待一段时间，确保对话框已聚焦
    time.sleep(1)

    # 在对话框中输入文本
    for char in text_to_type:
        keyboard.type(char)
        time.sleep(0.05)  # 适当延迟以避免过快输入
    # 模拟按下 Ctrl+V 粘贴剪贴板内容
    
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.2)

    # 按下 Enter 键
    #pyautogui.press('enter')
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

# 设置一个全局快捷键，例如 Alt+Q
keyboard.add_hotkey('ctrl+alt+q', paste_and_enter)

# 保持脚本运行，等待全局快捷键触发
keyboard.wait()

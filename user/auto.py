import time
from appium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

server = 'http://localhost:4723/wd/hub'
desired_caps = {
    "platformName": "Android",
    "platformVersion": "5.1.1",
    "deviceName": "127.0.0.1:62001",
    # 自动化测试包名
    "appPackage": "com.ss.android.ugc.trill",
    # 自动化测试Activity
    "appActivity": "com.ss.android.ugc.aweme.splash.SplashActivity",
    "automationName": "UiAutomator1",
    # 再次启动不需要再次安装
    "noReset": True,
    # unicode键盘 我们可以输入中文
    "unicodeKeyboard": True,
    # 操作之后还原回原先的输入法
    "resetKeyboard": True
}
driver = webdriver.Remote(server, desired_caps)
wait = WebDriverWait(driver, 15)
# 弹出框点击取消按钮
try:
    driver.find_element_by_id('com.ss.android.ugc.trill:id/sy')
except NoSuchElementException:
    pass
else:
    driver.find_element_by_id('com.ss.android.ugc.trill:id/sy').click()
# 点击首页搜索图标
wait.until(EC.presence_of_element_located(
    (By.XPATH, "//*[@resource-id='com.ss.android.ugc.trill:id/bjs']/android.widget.FrameLayout[2]"))).click()
# # 搜索输入框输入关键字
wait.until(EC.presence_of_element_located((By.ID, 'com.ss.android.ugc.trill:id/ac_'))).clear().send_keys('成都')
# # 然后点击搜索按钮
wait.until(EC.presence_of_element_located((By.ID, 'com.ss.android.ugc.trill:id/dfk'))).click()
# # 点击用户选项卡
wait.until(EC.presence_of_element_located((By.XPATH, "//*[@text='USERS']"))).click()
# 循环
for p in range(2):
    # 点击进入第1个用户
    time.sleep(1)
    wait.until(EC.presence_of_element_located(
        (By.XPATH, "//*[@resource-id='com.ss.android.ugc.trill:id/bc2']/android.widget.LinearLayout[1]"))).click()
    # 点击喜欢选项卡
    wait.until(EC.presence_of_element_located(
        (By.XPATH, "//*[@resource-id='com.ss.android.ugc.trill:id/cwn']/android.widget.RelativeLayout[2]"))).click()
    # 返回
    driver.find_element_by_id('com.ss.android.ugc.trill:id/ik').click()
    # 向上滑动一条用户信息
    destination_el = wait.until(EC.presence_of_element_located(
        (By.XPATH, "//*[@resource-id='com.ss.android.ugc.trill:id/bc2']/android.widget.LinearLayout[1]")))
    origin_el = wait.until(EC.presence_of_element_located(
        (By.XPATH, "//*[@resource-id='com.ss.android.ugc.trill:id/bc2']/android.widget.LinearLayout[2]")))
    driver.scroll(origin_el, destination_el)
# 退出
driver.quit()
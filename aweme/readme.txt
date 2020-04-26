夜神模拟器台湾版（分辨率设置-手机版-720*1280，关闭定位，语言设置为英语）
TikTok版本15.7.43
1、启动抓包：mitmdump -s D:\PycharmProjects\TikTok\aweme\crawler.py
2、启动appium服务
3、执行模拟点击：python D:\PycharmProjects\TikTok\aweme\auto.py
注：连接模拟器：adb connect 127.0.0.1:62001
    获取'deviceName'，使用命令：adb devices
   获取到'appPackage'和'appActivity'，adb连接上设备后打开应用，使用命令：adb shell dumpsys activity top|findstr ACTIVITY
   模拟器登录Play Store（账号cd30kt@gmail.com/30kt666666）安装TikTok
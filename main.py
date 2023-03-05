"""
这里是程序的入口！
"""

from PySide2.QtWidgets import QApplication
from PySide2.QtWidgets import QWidget
from sys import argv
import json

from MainWidget import Ui_MainWidget
from Form_Config import Ui_Form_Config
from chatbot import Bot


class MainWidget(QWidget, Ui_MainWidget):
    def __init__(self):
        super(MainWidget, self).__init__()
        self.ui = Ui_MainWidget()
        self.ui.setupUi(self)


class Form_Config(QWidget, Ui_Form_Config):
    def __init__(self):
        super(Form_Config, self).__init__()
        self.ui = Ui_Form_Config()
        self.ui.setupUi(self)


class Main:
    """
    程序主逻辑在此
    """
    def __init__(self):
        # 窗口展示
        self.window = MainWidget()
        self.window.show()
        self.window_config = Form_Config()

        # 绑定信号和槽
        self.window.ui.pushButton_config.clicked.connect(self.window_config.show)
        self.window.ui.pushButton_send.clicked.connect(self.send)
        self.window.ui.lineEdit_input.returnPressed.connect(self.send)

        self.window_config.ui.pushButton_save.clicked.connect(self.save)

        # 读取或写入设置
        try:
            with open(file="fanbot_config.json", mode="r", encoding="utf-8") as f:
                temp = f.read()
                json_f: dict = json.loads(temp)
            self.window_config.ui.lineEdit_botName.setText(json_f["botName"])
            self.window_config.ui.lineEdit_userName.setText(json_f["userName"])
            self.window_config.ui.checkBox_stopLearn.setChecked(json_f["stopLearn"])
        except:
            self.window_config.ui.lineEdit_botName.setText("FanBot")
            self.window_config.ui.lineEdit_userName.setText("Mango")
            self.window_config.ui.checkBox_stopLearn.setChecked(False)

        # 创建 Bot 对象
        self.bot = Bot(self.window_config.ui.lineEdit_botName.text(),
                       self.window_config.ui.checkBox_stopLearn.text(),
                       False)

    def send(self):
        """
        将输入框中的内容发送给 ChatBot，ChatBot 将进行回答。

        此方法同时被绑定在按钮“<<”上和按键 Enter 上，即敲击回车也可以发送消息。

        会在聊天框中打印信息。

        :return: None
        """
        question = self.window.ui.lineEdit_input.text()

        allow = False  # 标识符，如果输入的内容没有意义则拒绝发送

        for word in question:
            if not word == " ":
                allow = True  # 只要输入的内容有意义，则标识符改为 True，允许发送

        if not allow:
            return None  # 内容无意义，不予发送

        # 在聊天框打印用户发送的消息，然后清空输入框
        self.window.ui.textBrowser.append(f"{self.window_config.ui.lineEdit_userName.text()}\n<<<\t" + question)
        self.window.ui.lineEdit_input.clear()

        # 获取 ChatBot 的回答，并且打印在聊天框
        response = str(self.bot.chatbot.get_response(question))
        self.window.ui.textBrowser.append(f"{self.window_config.ui.lineEdit_botName.text()}\n>>>\t" + response + "\n")

        return None

    def save(self):
        """
        保存对设置所做的更改，点击保存按钮时。

        :return: None
        """
        del self.bot

        botName = self.window_config.ui.lineEdit_botName.text()
        userName = self.window_config.ui.lineEdit_userName.text()
        stopLearn = self.window_config.ui.checkBox_stopLearn.isChecked()

        self.bot = Bot(botName, stopLearn, False)

        # 设置写入到配置文件
        json_f = {"botName": botName, "userName": userName, "stopLearn": stopLearn}

        with open(file="fanbot_config.json", mode="w", encoding="utf-8") as f:
            f.write(json.dumps(json_f))

        return None

    def rollback(self):
        """
        完全重置机器人的一切训练成果。

        :return: None
        """
        del self.bot
        self.bot = Bot(self.window_config.ui.lineEdit_botName.text(),
                       self.window_config.ui.checkBox_stopLearn.isChecked(),
                       True)
        return None


if __name__ == "__main__":
    app = QApplication(argv)
    main = Main()
    exit_info = app.exec_()

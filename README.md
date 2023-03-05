## 项目介绍

这就是一个非常普通的，基于 ChatterBot 实现的聊天机器人，套上 PySide2 的窗口，瞎写成的简易聊天机器人。

此项目拥有一个不成熟的网页版，基于 Flask 和 Mongodb 数据库： bot.fancraft.top 。

## 使用说明

使用 `pip install -r requirments.txt` 以安装 chatterbot 和 pyside2，建议使用镜像源加速安装。

安装完毕后，首先运行根目录下的 `chatbot.py`，这将会在根目录下生成聊天机器人训练的数据库 `db.sqlite3`。

* 注意！由于语料的量非常大，这个过程会很漫长！你可以离开电脑去别的地方玩一会儿的，真的，绝对来得及！

命令行会打印出训练进度，等待训练完毕后会自动进入交互式聊天模式。此时可以退出命令行。

接下来，运行根目录下的 `main.py`，可视化窗口将会打开，您可以从窗口中进行聊天交互。

----

训练数据库大小超过 GitHub 的限制（100 MB）因此无法上传至仓库，还请见谅！

由于数据过于庞大（没错，这么点数据过于庞大），运行时可能会异常卡顿，我无能为力……

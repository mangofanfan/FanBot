## 项目介绍

这就是一个非常普通的，基于 ChatterBot 实现的聊天机器人，套上 PySide2 的窗口，瞎写成的简易聊天机器人。

此项目拥有一个不成熟的网页版，基于 Flask 和 Mongodb 数据库： bot.fancraft.top 。

项目基于 Python 3.6 开发。

## 使用说明

使用 `pip install -r requirments.txt` 以安装 chatterbot 和 pyside2，建议使用镜像源加速安装。

当然，如果您的网络不大好的话，这边是使用镜像源的命令：

    pip install -r requirments.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

安装完毕后，首先运行根目录下的 `chatbot.py`，这将会在根目录下生成聊天机器人训练的数据库 `db.sqlite3`。

* 注意！由于语料的量非常大，这个过程会很漫长！你可以离开电脑去别的地方玩一会儿的，真的，绝对来得及！

命令行会打印出训练进度，等待训练完毕后会自动进入交互式聊天模式。此时可以退出命令行。

接下来，运行根目录下的 `main.py`，可视化窗口将会打开，您可以从窗口中进行聊天交互。

----

训练数据库大小超过 GitHub 的限制（100 MB）因此无法上传至仓库，还请见谅！

由于数据过于庞大（没错，这么点数据过于庞大），运行时可能会异常卡顿，我无能为力……

## 错误修复

由于数据量问题，机器人无法做到秒级的响应，在可视化窗口（`main.py`）中进行交互聊天时每一次输入都可能造成一定时长的卡顿，相信我，这是正常现象……

    因为整个程序只有一个进程一个线程，卡顿当然是正常的了 TT

----

如果 Windows 平台在安装依赖库时报错，大概率是由于 Microsoft Visual C++ Build 工具没有安装：

    error: Microsoft Visual C++ 14.0 is required. Get it with "Microsoft Visual C++ Build Tools"

微软官网给的下载工具可能会出问题，可以从此处（以及更多地方都可以）下载需要的编译工具：https://blog.csdn.net/love906897406/article/details/125355524

安装完毕后，再次执行 `pip` 命令应当不会再报错。

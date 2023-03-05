"""
ChatterBot 启动
"""

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer


class Bot:
    def __init__(self, name: str, read_only: bool, retrain: bool):
        self.chatbot = ChatBot(name,
                               read_only=read_only,
                               logic_adapters=[
                                   {
                                       'import_path': 'chatterbot.logic.BestMatch'
                                   },
                               ]
                               )
        self.trainer = ChatterBotCorpusTrainer(self.chatbot)
        self.trainer_2 = ListTrainer(self.chatbot)

        # 根据用户指令决定是否重新训练语料
        if retrain:
            self.train()

    def train(self):

        # 读取语料库并进行训练，会花很久时间！
        with open(file="languages_train/datas.txt", mode="r", encoding="utf-8") as f:
            datas = []

            # 逐行处理语料
            for line in f.readlines():
                if line[0] == "E":
                    pass
                elif line[0] == "M":
                    datas.append(line.replace("M ", "").replace("\n", ""))

        # 分块训练，鉴于语料库太大所以分块的话能让用户更有等头（
        i = 0
        a = len(datas)
        c = 500
        t = a // c + 1

        while True:
            if (i + 1) * c > a:
                e = a
            else:
                e = (i + 1) * c

            print(f"\n训练第三方语料库中，当前为第 {i} 次训练，共需要训练 {t} 次。")
            datas_temp = datas[i * c: e]
            self.trainer_2.train(datas_temp)

            i += 1

            if e == a:
                break

        return None


if __name__ == "__main__":
    bot = Bot("FanBot", True, True)
    while True:
        question = input(">>>")
        response = bot.chatbot.get_response(question)
        print(response)
        print("\n")

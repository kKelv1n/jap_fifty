from enum import Enum
from jap_fifty import data
import random


class QuestionType(Enum):
    AskRomaA = 1
    AskRomaB = 2
    AskHiraganaA = 3
    AskHiraganaB = 4
    AskKatakanaA = 5
    AskKatakanaB = 6


class QuestionItf(object):

    def __init__(self):
        self.r, self.h, self.k = self.rand_data()
        self.q_type = None
        self.gen_data()

    def gen_data(self):
        pass

    # 根据平假名问罗马音
    def ask_roma_a(self):
        pass

    # 根据片假名问罗马音
    def ask_roma_b(self):
        pass

    # 根据罗马音问平假名
    def ask_hiragana_a(self):
        pass

    # 根据片假名问平假名
    def ask_hiragana_b(self):
        pass

    # 根据罗马音问片假名
    def ask_katakana_a(self):
        pass

    # 根据平假名问片假名
    def ask_katakana_b(self):
        pass

    def is_right(self, user_input: str) -> (bool, str):
        pass

    @staticmethod
    def rand_data() -> (str, str, str):
        x, y = random.randint(0, len(data.roma)-1), random.randint(0, len(data.roma[0])-1)
        return data.roma[x][y], data.hiragana[x][y], data.katakana[x][y]


# 问答
class QuestionA(QuestionItf):

    def __init__(self):
        super().__init__()

    def gen_data(self):
        pass

    def ask_roma_a(self):
        self.q_type = QuestionType.AskRomaA
        print("{}的罗马音是什么？".format(self.h))

    def ask_roma_b(self):
        self.q_type = QuestionType.AskRomaB
        print("{}的罗马音是什么？".format(self.k))

    def ask_hiragana_a(self):
        self.q_type = QuestionType.AskHiraganaA
        print("{}的平假名是什么？".format(self.r))

    def ask_hiragana_b(self):
        self.q_type = QuestionType.AskHiraganaB
        print("{}的平假名是什么？".format(self.k))

    def ask_katakana_a(self):
        self.q_type = QuestionType.AskKatakanaA
        print("{}的片假名是什么？".format(self.r))

    def ask_katakana_b(self):
        self.q_type = QuestionType.AskKatakanaB
        print("{}的片假名是什么？".format(self.h))

    def is_right(self, user_input: str) -> (bool, str):
        if self.q_type == QuestionType.AskRomaA or self.q_type == QuestionType.AskRomaB:
            return user_input == self.r, self.r
        elif self.q_type == QuestionType.AskHiraganaA or self.q_type == QuestionType.AskHiraganaB:
            return user_input == self.h, self.h
        else:
            return user_input == self.k, self.k


quest_a = QuestionA()

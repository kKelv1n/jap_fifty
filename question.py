from enum import Enum
from jap_fifty import data
from jap_fifty import utils

n = len(data.roma)
m = len(data.roma[0])


class QuestionType(Enum):
    AskRomaByHiragana = 1
    AskRomaByKatakana = 2
    AskHiraganaByRoma = 4
    AskHiraganaByKatakana = 4
    AskKatakanaByRoma = 5
    AskKatakanaByHiragana = 6


class Question(Enum):
    ask_roma = '{}的罗马音是什么？'
    ask_hiragana = '{}的平假名是什么？'
    ask_katakana = '{}的片假名是什么？'



def _get_data(x: int, y: int) -> (str, str, str):
    return data.roma[x][y], data.hiragana[x][y], data.katakana[x][y]


def _rand_data() -> (str, str, str):
    x, y = utils.rand_idx(n, m)
    return _get_data(x, y)


class QuestionItf(object):

    def __init__(self):
        self._x, self._y = utils.rand_idx(n, m)
        self._r, self._h, self._k = _get_data(self._x, self._y)
        self.q_type = None
        self._gen_data()


    def _gen_data(self):
        pass

    def _do_before_print_msg(self):
        pass

    def _do_after_print_msg(self):
        pass

    # 根据平假名问罗马音
    def ask_roma_by_hiragana(self):
        self.q_type = QuestionType.AskRomaByHiragana
        self._do_before_print_msg()
        print(Question.ask_roma.value.format(self._h))
        self._do_after_print_msg()

    # 根据片假名问罗马音
    def ask_roma_by_katakana(self):
        self.q_type = QuestionType.AskRomaByKatakana
        self._do_before_print_msg()
        print(Question.ask_roma.value.format(self._k))
        self._do_after_print_msg()

    # 根据罗马音问平假名
    def ask_hiragana_by_roma(self):
        self.q_type = QuestionType.AskHiraganaByRoma
        self._do_before_print_msg()
        print(Question.ask_hiragana.value.format(self._r))
        self._do_after_print_msg()

    # 根据片假名问平假名
    def ask_hiragana_by_katakana(self):
        self.q_type = QuestionType.AskHiraganaByKatakana
        self._do_before_print_msg()
        print(Question.ask_hiragana.value.format(self._k))
        self._do_after_print_msg()

    # 根据罗马音问片假名
    def ask_katakana_by_roma(self):
        self.q_type = QuestionType.AskKatakanaByRoma
        self._do_before_print_msg()
        print(Question.ask_katakana.value.format(self._r))
        self._do_after_print_msg()

    # 根据平假名问片假名
    def ask_katakana_by_hiragana(self):
        self.q_type = QuestionType.AskKatakanaByHiragana
        self._do_before_print_msg()
        print(Question.ask_katakana.value.format(self._h))
        self._do_after_print_msg()

    def is_right(self, user_input: str) -> (bool, str):
        pass


# Q&A
class QA(QuestionItf):

    def __init__(self):
        super().__init__()

    def is_right(self, user_input: str) -> (bool, str):
        if self.q_type == QuestionType.AskRomaByHiragana or self.q_type == QuestionType.AskRomaByKatakana:
            return user_input == self._r, self._r
        elif self.q_type == QuestionType.AskHiraganaByRoma or self.q_type == QuestionType.AskHiraganaByKatakana:
            return user_input == self._h, self._h
        else:
            return user_input == self._k, self._k


class Selection(QuestionItf):
    a = 97

    def __init__(self):
        self.__choice_num = 4
        self.__choices = {}
        self.__right_key = ''
        self.__check_choice_num()
        super().__init__()

    def __check_choice_num(self):
        max_num, min_num = 26, 4
        if self.__choice_num > max_num:
            self.__choice_num = max_num
        elif self.__choice_num <= 0:
            self.__choice_num = min_num


    def __set_right_choice(self):
        offset = utils.rand_n(self.__choice_num)
        self.__right_key = str(chr(self.a+offset))
        if self.q_type == QuestionType.AskRomaByHiragana or self.q_type == QuestionType.AskRomaByKatakana:
            self.__choices[self.__right_key] = self._r
        elif self.q_type == QuestionType.AskHiraganaByRoma or self.q_type == QuestionType.AskHiraganaByKatakana:
            self.__choices[self.__right_key] = self._h
        else:
            self.__choices[self.__right_key] = self._k

    def __set_other_choices(self):
        used_x, used_y = [self._x], [self._y]
        for key, val in self.__choices.items():
            if key == self.__right_key:
                continue
            x, y = utils.rand_idx_exclude(n, m, used_x, used_y)
            used_x.append(x)
            used_y.append(y)
            r, h, k = _get_data(x, y)
            if self.q_type == QuestionType.AskRomaByHiragana or self.q_type == QuestionType.AskRomaByKatakana:
                self.__choices[key] = r
            elif self.q_type == QuestionType.AskHiraganaByRoma or self.q_type == QuestionType.AskHiraganaByKatakana:
                self.__choices[key] = h
            else:
                self.__choices[key] = k

    def __gen_choices(self):
        self.__set_right_choice()
        self.__set_other_choices()

    def _gen_data(self):
        for i in range(self.__choice_num):
            self.__choices[str(chr(self.a + i))] = ''

    def __print_choices(self):
        choices_format = ''
        choice_vals = []
        for k, v in self.__choices.items():
            choice_vals.append(k)
            choice_vals.append(v)
            choices_format += '{}: {}   '
        print(choices_format.format(*choice_vals))

    def _do_after_print_msg(self):
        self.__print_choices()

    def _do_before_print_msg(self):
        self.__gen_choices()

    def is_right(self, user_input: str) -> (bool, str):
        return user_input == self.__right_key, self.__right_key



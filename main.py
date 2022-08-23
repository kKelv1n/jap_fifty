from jap_fifty.question import *


def print_result(is_right: bool, right_ans: str):
    if is_right:
        print("right！")
    else:
        print("wrong!!! answer is: ", right_ans)
    print("===============")


def ask_h_by_r(q: QuestionItf):
    q.ask_hiragana_by_roma()
    is_right, ans = q.is_right(input())
    print_result(is_right, ans)


def ask_k_by_r(q: QuestionItf):
    q.ask_katakana_by_roma()
    is_right, ans = q.is_right(input())
    print_result(is_right, ans)


def ask_r_by_h(q: QuestionItf):
    q.ask_roma_by_hiragana()
    is_right, ans = q.is_right(input())
    print_result(is_right, ans)


def ask_k_by_h(q: QuestionItf):
    q.ask_katakana_by_hiragana()
    is_right, ans = q.is_right(input())
    print_result(is_right, ans)


def ask_r_by_k(q: QuestionItf):
    q.ask_roma_by_katakana()
    is_right, ans = q.is_right(input())
    print_result(is_right, ans)


def ask_h_by_k(q: QuestionItf):
    q.ask_hiragana_by_katakana()
    is_right, ans = q.is_right(input())
    print_result(is_right, ans)


if __name__ == '__main__':
    while True:
        q = Selection()
        ask_h_by_r(q)
        ask_k_by_r(q)
        ask_k_by_h(q)
        ask_r_by_h(q)
        ask_r_by_k(q)
        ask_h_by_k(q)



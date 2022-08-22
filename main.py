from jap_fifty.question import QuestionA



if __name__ == '__main__':
    while True:
        q = QuestionA()
        q.ask_hiragana_a()
        is_right, ans = q.is_right(input())
        if is_right:
            print("right！")
        else:
            print("wrong!!! answer is: ", ans)
        print("===============")

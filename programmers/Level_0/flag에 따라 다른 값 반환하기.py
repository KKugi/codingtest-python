# 두 정수 a, b와 boolean 변수 flag가 매개변수로 주어질 때,
# flag가 true면 a + b를 false면 a - b를
# return 하는 solution 함수를 작성해 주세요.


def solution(a, b, flag):
    if flag:
        answer = a + b
    else:
        answer = a - b

    return answer


if __name__ == "__main__":
    a = -4
    b = 7
    flag = True

    answer = solution(a, b, flag)
    print(answer)

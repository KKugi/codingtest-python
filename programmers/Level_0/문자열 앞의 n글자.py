# 문자열 my_string과 정수 n이 매개변수로 주어질 때,
# my_string의 앞의 n글자로 이루어진 문자열을
# return 하는 solution 함수를 작성해 주세요.


def solution(my_string, n):
    answer = my_string[:n]
    return answer


if __name__ == "__main__":
    my_string = "ProgrammerS123"
    n = 11

    answer = solution(my_string, n)
    print(answer)

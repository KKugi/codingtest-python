# 정수가 담긴 리스트 num_list가 주어질 때,
# 모든 원소들의 곱이 모든 원소들의 합의 제곱보다 작으면 1을 크면 0을
# return하도록 solution 함수를 완성해주세요.


def solution(num_list):
    s_answer = 0
    m_answer = 1

    for i in range(len(num_list)):
        s_answer += num_list[i]
        m_answer *= num_list[i]

    if m_answer < s_answer**2:
        answer = 1
    else:
        answer = 0

    return answer


if __name__ == "__main__":
    num_list = [3, 4, 5, 2, 1]
    answer = solution(num_list)
    print(answer)

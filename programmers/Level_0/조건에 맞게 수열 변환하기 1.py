# 정수 배열 arr가 주어집니다.
# arr의 각 원소에 대해 값이 50보다 크거나 같은 짝수라면 2로 나누고,
# 50보다 작은 홀수라면 2를 곱합니다.
# 그 결과인 정수 배열을 return 하는 solution 함수를 완성해 주세요.


def solution(arr):
    for i in range(len(arr)):
        if arr[i] >= 50 and arr[i] % 2 == 0:
            arr[i] = arr[i] // 2

        elif arr[i] < 50 and arr[i] % 2 != 0:
            arr[i] = arr[i] * 2

        answer = arr
    return answer


if __name__ == "__main__":
    arr = [1, 2, 3, 100, 99, 98]
    answer = solution(arr)
    print(answer)

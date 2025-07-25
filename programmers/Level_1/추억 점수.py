# 사진들을 보며 추억에 젖어 있던 루는 사진별로 추억 점수를 매길려고 합니다.
# 사진 속에 나오는 인물의 그리움 점수를 모두 합산한 값이 해당 사진의 추억 점수가 됩니다.
# 예를 들어 사진 속 인물의 이름이 ["may", "kein", "kain"]이고 각 인물의 그리움 점수가 [5점, 10점, 1점]일 때
# 해당 사진의 추억 점수는 16(5 + 10 + 1)점이 됩니다.
# 다른 사진 속 인물의 이름이 ["kali", "mari", "don", "tony"]이고 ["kali", "mari", "don"]의 그리움 점수가 각각 [11점, 1점, 55점]]이고,
# "tony"는 그리움 점수가 없을 때, 이 사진의 추억 점수는 3명의 그리움 점수를 합한 67(11 + 1 + 55)점입니다.

# 그리워하는 사람의 이름을 담은 문자열 배열 name,
# 각 사람별 그리움 점수를 담은 정수 배열 yearning,
# 각 사진에 찍힌 인물의 이름을 담은 이차원 문자열 배열 photo가 매개변수로 주어질 때,
# 사진들의 추억 점수를 photo에 주어진 순서대로 배열에 담아 return하는 solution 함수를 완성해주세요.


# 방법1
# def solution(name, yearning, photo):
#     answer = []
#     matching = dict(zip(name, yearning))
#     for i in photo:
#         sum = 0
#         for j in i:
#             sum += matching.get(j, 0)

#         answer.append(sum)
#     return answer


# answer = solution(name, yearning, photo)
# print(answer)


# 방법2
def solution(name, yearning, photo):
    matching = {}
    for i in range(len(name)):
        matching[name[i]] = yearning[i]

    answer = []
    for i in photo:
        sum = 0
        for j in i:
            if j in matching:
                sum += matching[j]
        answer.append(sum)
    return answer


if __name__ == "__main__":
    name = ["may", "kein", "kain", "radi"]
    yearning = [5, 10, 1, 3]
    photo = [
        ["may", "kein", "kain", "radi"],
        ["may", "kein", "brin", "deny"],
        ["kon", "kain", "may", "coni"],
    ]

    answer = solution(name, yearning, photo)
    print(answer)

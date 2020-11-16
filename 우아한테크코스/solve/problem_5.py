# def solution(penter, pexit, pescape, data):
#     answer = ""
#     answer += penter
#     len_penter = len(penter)
#     print(len_penter)
#     for i in range(len(data)//len_penter):
#         if data[len_penter * i:len_penter * (i + 1)] in (penter, pexit, pescape):
#             answer += pescape
#         answer += data[len_penter * i:len_penter * (i + 1)]
#     answer += pexit
#     return answer


def solution(penter, pexit, pescape, data):
    answer = ""
    answer += penter
    for i in range(len(data) // len(penter)):
        if data[len(penter) * i : len(penter) * (i+1)] in (penter, pexit, pescape):
            answer += pescape
        answer += data[len(penter) * i : len(penter) * (i+1)]
    answer += pexit
    return answer


print(solution("1100","0010","1001","1101100100101111001111000000"))
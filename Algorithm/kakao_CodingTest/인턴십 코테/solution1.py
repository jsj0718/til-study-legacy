def editDistance(source, target):
    source_code = []
    target_code = []
    equal_list = []
    cnt = 0

    for s in source:
        source_code.append(ord(s) % 26)
    for t in target:
        target_code.append(ord(t) % 26)
    
    for i in range(26):
        for s in source_code:
            for t in target_code:
                if s == t:
                    cnt += 1
            equal_list.append(cnt)
            cnt = 0
            s += 1
            
    return equal_list


print(editDistance("aba", "caa"))



# def editDistance(source, target):
#     # Write your code here
#     fit_max = 0
#     length = len(source)
#     # create code
#     source_code = []
#     target_code = []
#     for s in source:
#         source_code.append(ord(s) % 26)
#     for t in target:
#         target_code.append(ord(t) % 26)
#     # shift source & comparison
#     for i in range(26):
#         fit = 0
#         target_idx = -1
#         for source_idx in range(length):
#             while target_idx < length:
#                 target_idx += 1
#                 if (source_code[source_idx] + i) % 26 == target_code[target_idx]:
#                     fit += 1
#                     break
#                 else: break
                
#         if fit > fit_max:
#             fit_max = fit
#     # result
#     result = (length - fit_max) * 2
#     return result
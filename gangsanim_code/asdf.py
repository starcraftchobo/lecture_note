# t = 'TTTTTTABC'
# p = 'TTA'
# N = len(t)
# M = len(p)
# cnt = 0
# for i in range(N-M+1):
#     for j in range(M):
#         if t[i+j] != p[h]:
#             break
#     else:
#         cnt += 1
#
# print(cnt)

target = 'Hello SSAFY 12th!'
pattern = 'SSA'

def BruteForce(pat, text):
    N = len(text)
    M = len(pat)
    i = 0
    j = 0

    while j < M and i < N:

        if text[i] != pat[j]:
            i = i -j    # 현재위치로 복귀
            j = -1      # j를 0으로 복귀

    i = i+1
    j = j+1

    if j == M:
        return i - M
    else:
        return -1

#simple version
text = 'this is simple version'
pattern = 'si'
def BruteForceV2(pat, text):
    for idx in range(len(text)-len(pat)+1):
        # 패턴 처음부터 끝까지 순회
        for j in range(len(pattern)):
            # 1. 다르면 break
            if text[idx+1] != pat[j]:
                break
            # 2.
        else:
           return idx
    else:
        return -1
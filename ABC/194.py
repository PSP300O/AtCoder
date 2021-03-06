# # A ======================
# def asolve():
#     a, b = map(int, input().split())
#     if a + b >= 15 and b >= 8:
#         return 1
#     elif a + b >= 10 and b >= 3:
#         return 2
#     elif a + b >= 3:
#         return 3
#     else:
#         return 4

# print(asolve())

# # B ======================
# def bsolve():
#     n = int(input())
#     a, b = [], []
#     c = []
#     ans = [10**5 for _ in range(4)]
#     ansno = [-1, -1, -1, -1]
#     for i in range(n):
#         aa, bb = map(int, input().split())
#         a.append(aa)
#         b.append(bb)
#         c.append(aa + bb)
#         if aa < ans[1]:
#             if aa < ans[0]:
#                 ans[1] = ans[0]
#                 ans[0] = aa
#                 ansno[1] = ansno[0]
#                 ansno[0] = i
#             else:
#                 ans[1] = aa
#                 ansno[1] = i
#         if bb < ans[3]:
#             if bb < ans[2]:
#                 ans[3] = ans[2]
#                 ans[2] = bb
#                 ansno[3] = ansno[2]
#                 ansno[2] = i
#             else:
#                 ans[3] = bb
#                 ansno[3] = i
#     aaa = 0

#     if ansno[0] == ansno[2]:
#         aaa = min(max(ans[0], ans[3]), max(ans[1], ans[2]))
#     else:
#         aaa = max(ans[0], ans[2])

#     if aaa < min(c):
#         return aaa
#     else:
#         return min(c)

# print(bsolve())

# # C ======================
# def csolve():
#     n = int(input())
#     a = list(map(int, input().split()))
#     ans = 0
#     b = [0 for _ in range(401)]
#     for A in a:
#         A += 200
#         b[A] += 1
#     for i in range(len(b)):
#         for j in range(i, len(b)):
#             ans += b[i] * b[j] * (j - i)**2
#     return ans

# print(csolve())


def dsolve():
    n = int(input())
    ans = 0
    save = -1
    counter = 0
    while ans != save:
        counter += 1
        save = ans
        ans += (counter * (1.0 / n)**counter)
    return ans


print(dsolve())
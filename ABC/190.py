# # A==================================
# def asolve():
#     a, b, c = map(int, input().split())
#     if a + c > b:
#         return 'Takahashi'
#     else:
#         return 'Aoki'

# print(asolve())
# # B==================================
# def bsolve():
#     n, s, d = map(int, input().split())
#     for _ in range(n):
#         x, y = map(int, input().split())
#         if x < s and d < y:
#             return True
#     return False

# if bsolve():
#     print('Yes')
# else:
#     print('No')
# # C===========================(解説参考)
# import itertools

# def csolve():
#     n, m = map(int, input().split())
#     cond = [tuple(map(int, input().split())) for _ in range(m)]
#     k = int(input())
#     choice = [tuple(map(int, input().split())) for _ in range(k)]
#     ans = 0
#     for balls in itertools.product(*choice):
#         balls = set(balls)
#         cnt = sum(a in balls and b in balls for a, b in cond)
#         if ans < cnt:
#             ans = cnt
#     return ans

# print(csolve())

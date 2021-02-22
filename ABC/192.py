# # A==============================
# def asolve():
#     x = int(input())
#     x %= 100
#     return 100 - x

# print(asolve())
# # B==============================
# def bsolve():
#     s = input()
#     for i in range(len(s)):
#         if i % 2 == 0 and not (ord('a') <= ord(s[i])
#                                and ord(s[i]) <= ord('z')):
#             return False
#         if i % 2 == 1 and not (ord('A') <= ord(s[i])
#                                and ord(s[i]) <= ord('Z')):
#             return False
#     return True


# if bsolve():
#     print('Yes')
# else:
#     print('No')
# # C==============================
def csolve():
    n, k = map(int, input().split())
    save = -1
    ak = n
    for i in range(k):
        save = ak
        ak = str(ak)
        m = ''.join(sorted(ak))
        M = ''.join(m[::-1])
        ak = int(M) - int(m)
        if ak == save:
            return ak
    return ak


print(csolve())
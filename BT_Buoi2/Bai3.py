def superpalindromesInRange(L, R):
    magic= 100000
    Ans = []

    def is_palindrome(x):
        x = str(x)
        return x == x[::-1]

    for k in range(magic):
        s = str(k)
        t = s + s[-2::-1]
        v = int(t) ** 2
        print(v, L, R, is_palindrome(v))
        if v > R: break
        if v >= L and is_palindrome(v):
            Ans.append(v)

    for k in range(magic):
        s = str(k)
        t = s + s[::-1]
        v = int(t) ** 2
        print(v, L, R, is_palindrome(v))
        if v > R: break
        if v >= L and is_palindrome(v):
            print(v)
            Ans.append(v)

    return Ans


L = int(input())
R = int(input())
ans = superpalindromesInRange(L, R)
print(ans)

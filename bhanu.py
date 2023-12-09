def bhanu(w, w_l):
    w.sort()
    v= 0
    l,r= 0, len(w) - 1

    while l <= r:
        if w[l] + w[r] <= w_l:
            l += 1
        r -= 1
        v+= 1

    return v

w = list(map(int, input().split()))
w_l = int(input())
o = bhanu(w, w_l)
print(o)


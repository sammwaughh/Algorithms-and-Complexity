# Rod Cutting

# Top Down
prices = [1,5,8,9,10,17,17,20,24,30]

def maxRevenue(p, n, r):
    if r[n] != -1:
        return r[n]
    if n == 0:
        q = 0
    else:
        q = -1
        for i in range(1,n+1):
            val = p[i-1] + maxRevenue(p, n-i, r)
            if val > q:
                q = val
    r[n] = q
    return q
    

for i in range(1,11):
    r = [-1]*(i+1)
    print("{0}: {1}".format(i, maxRevenue(prices, i, r)))



# Bottom Up
prices = [1,5,8,9,10,17,17,20,24,30]

def bottomUpRod(p, n):
    r = [0]*(n+1)
    for j in range(1, n+1):
        q = -1
        for i in range(1, j+1):
            val = p[i-1] + r[j-i]
            if val > q:
                q = val
        r[j] = q
    return r[n]

for i in range(1,11):
    print("{0}: {1}".format(i, bottomUpRod(prices, i)))
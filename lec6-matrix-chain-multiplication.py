# Optimal Matrix Chain Multiplications

# Top Down
p = [10,100,5,50]
n = len(p)-1

m = []
for i in range(n):
    row = []
    for j in range(n):
        row.append(None)
    m.append(row)

def mM(m, p, i, j):
    if m[i][j] != None:
        return m[i][j]
    if i == j:
        m[i][j] = 0
    else:
        q = None
        for k in range(i, j):
            if q != None:
                val = mM(m, p, i, k) + mM(m,p,k+1,j) + p[i-1]*p[k]*p[j]
                if val < q:
                    q = val
            else:
                q = mM(m, p, i, k) + mM(m,p,k+1,j) + p[i-1]*p[k]*p[j]
        m[i][j] = q
    return m[i][j]

#print(mM(m, p, 0, n-1))


# Bottom Up
p = [10,100,5,50]
n = len(p)-1

def mMBottomUp(p):
    m = []
    for i in range(n):
        row = []
        for j in range(n):
            if i == j:
                row.append(0)
            else:
                row.append(None)
        m.append(row)
    s = []
    r = [0]*n
    for i in range(n):
        s.append(r)
    
    for l in range(2, n+1):
        for i in range(n-l+1):
            j = i+l-1
            q = None
            for k in range(i, j):
                if q == None:
                    q = m[i][k]+m[k+1][j]+p[i-1]*p[k]*p[j]
                    s[i][j] = k
                else:
                    val = m[i][k]+m[k+1][j]+p[i-1]*p[k]*p[j]
                    if val < q:
                        q = val
                        s[i][j] = k
            m[i][j] = q
    return m, s

def printPar(s, i, j):
    if i == j:
        print("A_{}".format(i))
    else:
        p1 = printPar(s,i,s[i][j])
        p2 = printPar(s,s[i][j]+1,j)
        print("(" + p1 + p2 + ")")

res = mMBottomUp(p)
m = res[0]
s = res[1]
print(s)
print(m[0][n-1])
